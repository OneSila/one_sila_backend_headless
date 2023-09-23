from core.schema.types.types import auto
from core.schema.types.input import NodeInput, input, partial

from eancodes.models import EanCode


@input(EanCode, fields="__all__")
class EanCodeInput:
    pass


@partial(EanCode, fields="__all__")
class EanCodePartialInput(NodeInput):
    pass
