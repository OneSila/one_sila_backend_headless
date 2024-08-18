from django.db import transaction

from core.exceptions import SanityCheckError
from contacts.models import ShippingAddress
from shipments.models import Shipment, ShipmentItemToShip
from inventory.models import InventoryLocation
from shipments.exceptions import NoShippingAddressError, NotEnoughStockError

import logging

logger = logging.getLogger(__name__)


class ShipOrderSanityCheckMixin:
    def _sanity_check(self):
        if not self.order.is_to_ship():
            raise SanityCheckError(f"Cannot prepare order with status {self.order.status}")


class ShipmentForOrderItemFactory(ShipOrderSanityCheckMixin):
    """
    Ever order item needs shipping at some point.  We treat them one by one
    to ensure we can keep the relation with the order-item at all times.
    This goes for bundle items, and simple items.

    The items need to be assigned to a given shipping address.
    That means that we must order them by the preferred shipping address.

    Please note that this factory will refuse to ship an item if there
    is not enough inventory on hands to ship the orderitem completely.
    """

    def __init__(self, orderitem):
        self.orderitem = orderitem
        self.product = orderitem.product
        self.quantity = orderitem.quantity
        self.order = orderitem.order
        self.deliveryaddress = self.order.shipping_address
        self.multi_tenant_company = orderitem.multi_tenant_company
        self.country = self.order.shipping_address.country
        self.shipment_for_addresses = {}
        self.shipments = set()
        self.shipmentitems = []

    def _sanity_check(self):
        super()._sanity_check()

        quantity_available = self.product.inventory.physical()
        if self.quantity > quantity_available:
            msg = (
                f"Not enough stock to ship order {self.order} product {self.product}. "
                f"Needed: {self.quantity}. Available: {quantity_available}"
            )
            raise SanityCheckError(msg)

    def get_product_inventory(self, product, shippingaddress=None):
        # In order to prepare shipments we want to order the inventory for each item needed and give the most
        # relevant locations first. Remeber filter_physical is already deflating the products for you.
        qs = product.inventory.\
            filter_multi_tenant(self.multi_tenant_company).\
            filter_internal().\
            filter_physical()

        if shippingaddress:
            qs = qs.filter_shippingaddress(shippingaddress)

        return qs.order_by_relevant_shippinglocation(self.country)

    def set_orderitem_contents(self):
        """
        Before we know where we will ship from, we need to know what we'll be shipping on a high level.
        This is easy for simple and manufacturable products as we just one themselves with the quanity sold.
        But for bundles, that's a different question all together. They can contains bundles, simples,...
        All with their own quantities.

        Subselecting into supplier products where applicable we'll be doing in a different step.
        """
        if self.product.is_simple() or self.product.is_manufacturable():
            self.orderitem_contents = ((self.product, self.quantity),)
        elif self.product.is_bundle():
            bundle_variations = self.product.deflate_bundle()

            logger.debug(F"Deflated {self.product} and found {bundle_variations=}")

            items = {}
            for bv in bundle_variations:
                quantity_adjusted = bv.quantity * self.quantity
                try:
                    items[bv.variation] += quantity_adjusted
                except KeyError:
                    items[bv.variation] = quantity_adjusted

            orderitem_contents = [(i, q) for i, q in items.items()]
            logger.debug(F"Decided that the bundle is made of: {orderitem_contents=}")
            self.orderitem_contents = orderitem_contents
        else:
            raise ValueError(f"Product with type {self.product.type} is not supported.")

    def create_shipment_item(self, inv, quantity):
        shippingaddress = inv.inventorylocation.shippingaddress
        product = inv.product

        try:
            shipment = self.shipment_for_addresses[shippingaddress]
        except KeyError:
            # Ensure the shipment filtes on DRAFT.  We dont want to
            # be assigning items to ship to shipments that are already about to be shipped out.
            # This factory should be called by another more higher level piece of code.
            # that one has the responsability to mark the shipments ready for shipping once
            # its satisfied with the state of the goods.
            shipment, _ = Shipment.objects.get_or_create(
                multi_tenant_company=self.multi_tenant_company,
                from_address=shippingaddress,
                to_address=self.deliveryaddress,
                order=self.order,
                status=Shipment.DRAFT)
            self.shipments.add(shipment)
            self.shipment_for_addresses[shippingaddress] = shipment

        shipmentitem = shipment.shipmentitemtoship_set.create(
            multi_tenant_company=self.multi_tenant_company,
            product=product,
            quantity=quantity,
            orderitem=self.orderitem)
        self.shipmentitems.append(shipmentitem)

    @transaction.atomic
    def ship_items(self):
        """Since we now know what we need to ship, we need to figure out where we will ship from
        whilst prioritising the most useful shipping location.

        At the moment, that is based on the country. But needs serious work to make it 'intelligent'.

        We will create a shipment on the given shippingaddress of the best shipping location found
        for the quantity needed.
        """
        for item, quantity in self.orderitem_contents:
            # Get all of the low level items which will actually get shipped.
            # and iterate through them untill you run out of items to ship.
            inventory_list = list(self.get_product_inventory(item))

            logger.debug(f"About to create shipment item for {item=}")

            while quantity:
                try:
                    inv = inventory_list.pop()

                    if inv.quantity >= quantity:
                        self.create_shipment_item(inv, quantity)
                        logger.debug(f"Partial shipment created for {inv.product} with qty {quantity}. {inv=}")
                        quantity = 0
                    else:
                        self.create_shipment_item(inv, inv.quantity)
                        logger.debug(f"Final Partial or full shipment created for {inv.product} with qty {inv.quantity}. {inv=}")
                        quantity -= inv.quantity
                except IndexError as e:
                    msg = (
                        f"No more inventory available for {item=}. Quantity still needed: {quantity}."
                        "This should not happen as the SanityCheckError should have caught this item."
                    )
                    raise NotEnoughStockError(msg) from e

    def run(self):
        self._sanity_check()
        self.set_orderitem_contents()
        self.ship_items()


class PrepareShipmentsFactory(ShipOrderSanityCheckMixin):
    """
    Preparing an shipment:
    1. depends if the order is ready to ship (locally shippable items have enough inventory)
    2. will create a shipment for every item needed
    3. from any location found.

    This factory is used for both complete and partial orders.
    The actual shipping will happen in other flows.
    This factory will treat one order-item at a time. Why? Because we need to keep tracebility
    inside of the order what has been shipped and what not.
    """

    def __init__(self, order):
        self.multi_tenant_company = order.multi_tenant_company
        self.order = order
        self.orderitems = order.orderitem_set.all()
        self.country = order.shipping_address.country
        self.order_items = order.orderitem_set.all()
        self.shipments = []
        self.shipmentitems = []
        self.shipmentfororder_factories = []

    def populate_shipments(self):
        for item in self.orderitems:
            f = ShipmentForOrderItemFactory(item)
            f.run()
            self.shipmentfororder_factories.append(f)
            self.shipments.extend(f.shipments)
            self.shipmentitems.extend(f.shipmentitems)

        self.shipments = list(set(self.shipments))

    def run(self):
        self._sanity_check()
        self.populate_shipments()
