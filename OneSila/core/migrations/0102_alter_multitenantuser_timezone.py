# Generated by Django 5.0.2 on 2024-06-16 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0101_alter_multitenantuser_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multitenantuser',
            name='timezone',
            field=models.CharField(choices=[('Turkey', 'Turkey'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('Etc/GMT-1', 'Etc/GMT-1'), ('Asia/Baku', 'Asia/Baku'), ('America/Recife', 'America/Recife'), ('Europe/Prague', 'Europe/Prague'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('Australia/Perth', 'Australia/Perth'), ('Etc/GMT-7', 'Etc/GMT-7'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('America/St_Johns', 'America/St_Johns'), ('America/Managua', 'America/Managua'), ('America/Jujuy', 'America/Jujuy'), ('UCT', 'UCT'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('America/Rosario', 'America/Rosario'), ('Singapore', 'Singapore'), ('Africa/Bamako', 'Africa/Bamako'), ('America/Scoresbysund', 'America/Scoresbysund'), ('America/Montreal', 'America/Montreal'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('Asia/Baghdad', 'Asia/Baghdad'), ('Pacific/Majuro', 'Pacific/Majuro'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('Pacific/Truk', 'Pacific/Truk'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Europe/Sofia', 'Europe/Sofia'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('Europe/Vatican', 'Europe/Vatican'), ('Indian/Reunion', 'Indian/Reunion'), ('America/Belem', 'America/Belem'), ('America/Creston', 'America/Creston'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Asia/Gaza', 'Asia/Gaza'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('America/Antigua', 'America/Antigua'), ('Asia/Damascus', 'Asia/Damascus'), ('Africa/Lusaka', 'Africa/Lusaka'), ('America/Cayenne', 'America/Cayenne'), ('America/Martinique', 'America/Martinique'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('Europe/Skopje', 'Europe/Skopje'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Portugal', 'Portugal'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('Asia/Khandyga', 'Asia/Khandyga'), ('Asia/Samarkand', 'Asia/Samarkand'), ('America/Detroit', 'America/Detroit'), ('Asia/Makassar', 'Asia/Makassar'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('GB-Eire', 'GB-Eire'), ('Europe/Zagreb', 'Europe/Zagreb'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('Europe/Vaduz', 'Europe/Vaduz'), ('America/Miquelon', 'America/Miquelon'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('Asia/Amman', 'Asia/Amman'), ('America/Mendoza', 'America/Mendoza'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Asia/Taipei', 'Asia/Taipei'), ('Etc/GMT', 'Etc/GMT'), ('Asia/Muscat', 'Asia/Muscat'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('Asia/Seoul', 'Asia/Seoul'), ('Africa/Freetown', 'Africa/Freetown'), ('America/Knox_IN', 'America/Knox_IN'), ('America/Louisville', 'America/Louisville'), ('Greenwich', 'Greenwich'), ('Europe/Berlin', 'Europe/Berlin'), ('Australia/Adelaide', 'Australia/Adelaide'), ('W-SU', 'W-SU'), ('Egypt', 'Egypt'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('US/Alaska', 'US/Alaska'), ('Pacific/Ponape', 'Pacific/Ponape'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('America/Santiago', 'America/Santiago'), ('Africa/Bissau', 'Africa/Bissau'), ('America/Nome', 'America/Nome'), ('Europe/London', 'Europe/London'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('Pacific/Gambier', 'Pacific/Gambier'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Europe/Warsaw', 'Europe/Warsaw'), ('America/Montevideo', 'America/Montevideo'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Canada/Yukon', 'Canada/Yukon'), ('Africa/Maseru', 'Africa/Maseru'), ('Antarctica/Troll', 'Antarctica/Troll'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('Australia/NSW', 'Australia/NSW'), ('Zulu', 'Zulu'), ('Pacific/Fiji', 'Pacific/Fiji'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('US/Samoa', 'US/Samoa'), ('Etc/GMT+9', 'Etc/GMT+9'), ('Etc/GMT+12', 'Etc/GMT+12'), ('America/Havana', 'America/Havana'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('Etc/GMT+1', 'Etc/GMT+1'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('Indian/Comoro', 'Indian/Comoro'), ('America/Denver', 'America/Denver'), ('America/Shiprock', 'America/Shiprock'), ('Etc/GMT-14', 'Etc/GMT-14'), ('America/Paramaribo', 'America/Paramaribo'), ('America/Phoenix', 'America/Phoenix'), ('America/Eirunepe', 'America/Eirunepe'), ('Iceland', 'Iceland'), ('America/Godthab', 'America/Godthab'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('EST5EDT', 'EST5EDT'), ('America/Dawson', 'America/Dawson'), ('Asia/Thimphu', 'Asia/Thimphu'), ('Asia/Nicosia', 'Asia/Nicosia'), ('Europe/Bucharest', 'Europe/Bucharest'), ('Australia/Currie', 'Australia/Currie'), ('Etc/GMT+5', 'Etc/GMT+5'), ('America/Halifax', 'America/Halifax'), ('Asia/Macao', 'Asia/Macao'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('Europe/Athens', 'Europe/Athens'), ('Asia/Dubai', 'Asia/Dubai'), ('Libya', 'Libya'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Africa/Accra', 'Africa/Accra'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('Israel', 'Israel'), ('Asia/Yerevan', 'Asia/Yerevan'), ('America/Fortaleza', 'America/Fortaleza'), ('America/Lower_Princes', 'America/Lower_Princes'), ('America/Pangnirtung', 'America/Pangnirtung'), ('America/El_Salvador', 'America/El_Salvador'), ('Australia/ACT', 'Australia/ACT'), ('America/Anchorage', 'America/Anchorage'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('GMT', 'GMT'), ('MST7MDT', 'MST7MDT'), ('Pacific/Saipan', 'Pacific/Saipan'), ('America/Inuvik', 'America/Inuvik'), ('Europe/Chisinau', 'Europe/Chisinau'), ('America/Guatemala', 'America/Guatemala'), ('America/Ensenada', 'America/Ensenada'), ('US/Michigan', 'US/Michigan'), ('Canada/Central', 'Canada/Central'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('Canada/Eastern', 'Canada/Eastern'), ('Etc/GMT-3', 'Etc/GMT-3'), ('Africa/Douala', 'Africa/Douala'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('America/Edmonton', 'America/Edmonton'), ('Indian/Christmas', 'Indian/Christmas'), ('Australia/North', 'Australia/North'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('America/Montserrat', 'America/Montserrat'), ('Australia/Melbourne', 'Australia/Melbourne'), ('Asia/Omsk', 'Asia/Omsk'), ('America/Nuuk', 'America/Nuuk'), ('Europe/Riga', 'Europe/Riga'), ('Africa/Cairo', 'Africa/Cairo'), ('NZ-CHAT', 'NZ-CHAT'), ('America/Marigot', 'America/Marigot'), ('Asia/Atyrau', 'Asia/Atyrau'), ('America/Mexico_City', 'America/Mexico_City'), ('America/Bahia', 'America/Bahia'), ('Pacific/Kanton', 'Pacific/Kanton'), ('Etc/GMT+2', 'Etc/GMT+2'), ('WET', 'WET'), ('Chile/Continental', 'Chile/Continental'), ('America/Monterrey', 'America/Monterrey'), ('Africa/Algiers', 'Africa/Algiers'), ('America/Grenada', 'America/Grenada'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('PST8PDT', 'PST8PDT'), ('Indian/Chagos', 'Indian/Chagos'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('America/Vancouver', 'America/Vancouver'), ('Africa/Niamey', 'Africa/Niamey'), ('Europe/Samara', 'Europe/Samara'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Etc/Greenwich', 'Etc/Greenwich'), ('Asia/Tehran', 'Asia/Tehran'), ('America/Atikokan', 'America/Atikokan'), ('Asia/Singapore', 'Asia/Singapore'), ('Etc/GMT-13', 'Etc/GMT-13'), ('Pacific/Yap', 'Pacific/Yap'), ('Asia/Calcutta', 'Asia/Calcutta'), ('Europe/Simferopol', 'Europe/Simferopol'), ('Europe/Minsk', 'Europe/Minsk'), ('Europe/Volgograd', 'Europe/Volgograd'), ('US/Mountain', 'US/Mountain'), ('America/Glace_Bay', 'America/Glace_Bay'), ('America/Campo_Grande', 'America/Campo_Grande'), ('US/East-Indiana', 'US/East-Indiana'), ('Australia/Victoria', 'Australia/Victoria'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('CET', 'CET'), ('Africa/Bangui', 'Africa/Bangui'), ('Australia/Sydney', 'Australia/Sydney'), ('Indian/Maldives', 'Indian/Maldives'), ('Africa/Abidjan', 'Africa/Abidjan'), ('America/Whitehorse', 'America/Whitehorse'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('Asia/Vientiane', 'Asia/Vientiane'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('Asia/Jayapura', 'Asia/Jayapura'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('EET', 'EET'), ('Etc/GMT-12', 'Etc/GMT-12'), ('Europe/Zurich', 'Europe/Zurich'), ('Pacific/Guam', 'Pacific/Guam'), ('Africa/Djibouti', 'Africa/Djibouti'), ('Africa/Kampala', 'Africa/Kampala'), ('Africa/Blantyre', 'Africa/Blantyre'), ('Australia/Queensland', 'Australia/Queensland'), ('Asia/Harbin', 'Asia/Harbin'), ('America/Iqaluit', 'America/Iqaluit'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('GMT-0', 'GMT-0'), ('Europe/San_Marino', 'Europe/San_Marino'), ('America/Anguilla', 'America/Anguilla'), ('Europe/Tirane', 'Europe/Tirane'), ('Etc/GMT+7', 'Etc/GMT+7'), ('America/Caracas', 'America/Caracas'), ('America/Kralendijk', 'America/Kralendijk'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('Indian/Mauritius', 'Indian/Mauritius'), ('Iran', 'Iran'), ('US/Eastern', 'US/Eastern'), ('America/Yellowknife', 'America/Yellowknife'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('Europe/Budapest', 'Europe/Budapest'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Africa/Khartoum', 'Africa/Khartoum'), ('America/Sitka', 'America/Sitka'), ('Africa/Conakry', 'Africa/Conakry'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Africa/Maputo', 'Africa/Maputo'), ('US/Arizona', 'US/Arizona'), ('Asia/Karachi', 'Asia/Karachi'), ('Asia/Colombo', 'Asia/Colombo'), ('Europe/Busingen', 'Europe/Busingen'), ('Australia/Hobart', 'Australia/Hobart'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('Etc/GMT-2', 'Etc/GMT-2'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('Etc/Universal', 'Etc/Universal'), ('Asia/Qatar', 'Asia/Qatar'), ('America/Cuiaba', 'America/Cuiaba'), ('Africa/Dakar', 'Africa/Dakar'), ('Europe/Belfast', 'Europe/Belfast'), ('Etc/GMT+10', 'Etc/GMT+10'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('America/Porto_Velho', 'America/Porto_Velho'), ('America/Curacao', 'America/Curacao'), ('Pacific/Easter', 'Pacific/Easter'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Africa/Monrovia', 'Africa/Monrovia'), ('America/Juneau', 'America/Juneau'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('America/Belize', 'America/Belize'), ('Brazil/East', 'Brazil/East'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('GMT0', 'GMT0'), ('Europe/Vienna', 'Europe/Vienna'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('CST6CDT', 'CST6CDT'), ('Etc/GMT+6', 'Etc/GMT+6'), ('ROK', 'ROK'), ('Europe/Stockholm', 'Europe/Stockholm'), ('America/St_Thomas', 'America/St_Thomas'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Africa/Lome', 'Africa/Lome'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('Navajo', 'Navajo'), ('America/Moncton', 'America/Moncton'), ('Etc/Zulu', 'Etc/Zulu'), ('Pacific/Wallis', 'Pacific/Wallis'), ('America/Chihuahua', 'America/Chihuahua'), ('America/Indianapolis', 'America/Indianapolis'), ('Africa/Luanda', 'Africa/Luanda'), ('America/St_Kitts', 'America/St_Kitts'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('US/Hawaii', 'US/Hawaii'), ('America/Cayman', 'America/Cayman'), ('America/Adak', 'America/Adak'), ('Pacific/Auckland', 'Pacific/Auckland'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('America/Merida', 'America/Merida'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('Etc/UTC', 'Etc/UTC'), ('Antarctica/Davis', 'Antarctica/Davis'), ('America/Nipigon', 'America/Nipigon'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('America/Boa_Vista', 'America/Boa_Vista'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('Eire', 'Eire'), ('Atlantic/Canary', 'Atlantic/Canary'), ('Etc/GMT-8', 'Etc/GMT-8'), ('US/Central', 'US/Central'), ('Asia/Kuwait', 'Asia/Kuwait'), ('America/Tijuana', 'America/Tijuana'), ('Australia/West', 'Australia/West'), ('Africa/Juba', 'Africa/Juba'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('America/Resolute', 'America/Resolute'), ('Europe/Paris', 'Europe/Paris'), ('Africa/Libreville', 'Africa/Libreville'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('Asia/Chongqing', 'Asia/Chongqing'), ('Australia/Eucla', 'Australia/Eucla'), ('Europe/Andorra', 'Europe/Andorra'), ('GMT+0', 'GMT+0'), ('Pacific/Nauru', 'Pacific/Nauru'), ('Europe/Bratislava', 'Europe/Bratislava'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Pacific/Apia', 'Pacific/Apia'), ('America/St_Lucia', 'America/St_Lucia'), ('Asia/Tashkent', 'Asia/Tashkent'), ('America/Catamarca', 'America/Catamarca'), ('Asia/Urumqi', 'Asia/Urumqi'), ('America/Hermosillo', 'America/Hermosillo'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('Poland', 'Poland'), ('America/Jamaica', 'America/Jamaica'), ('Pacific/Palau', 'Pacific/Palau'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('America/Swift_Current', 'America/Swift_Current'), ('Asia/Almaty', 'Asia/Almaty'), ('Universal', 'Universal'), ('Asia/Chita', 'Asia/Chita'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Canada/Pacific', 'Canada/Pacific'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('America/Winnipeg', 'America/Winnipeg'), ('America/Yakutat', 'America/Yakutat'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('America/Menominee', 'America/Menominee'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Europe/Rome', 'Europe/Rome'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Europe/Madrid', 'Europe/Madrid'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('Asia/Kolkata', 'Asia/Kolkata'), ('Etc/GMT+4', 'Etc/GMT+4'), ('America/Tortola', 'America/Tortola'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Asia/Shanghai', 'Asia/Shanghai'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('Africa/Asmara', 'Africa/Asmara'), ('Asia/Dili', 'Asia/Dili'), ('America/Guadeloupe', 'America/Guadeloupe'), ('Mexico/General', 'Mexico/General'), ('America/Guyana', 'America/Guyana'), ('Jamaica', 'Jamaica'), ('Asia/Saigon', 'Asia/Saigon'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('Pacific/Efate', 'Pacific/Efate'), ('Pacific/Johnston', 'Pacific/Johnston'), ('Europe/Tallinn', 'Europe/Tallinn'), ('America/Ojinaga', 'America/Ojinaga'), ('America/Noronha', 'America/Noronha'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('Australia/Canberra', 'Australia/Canberra'), ('Cuba', 'Cuba'), ('PRC', 'PRC'), ('Africa/Gaborone', 'Africa/Gaborone'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('Australia/Tasmania', 'Australia/Tasmania'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('America/St_Vincent', 'America/St_Vincent'), ('Asia/Bishkek', 'Asia/Bishkek'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('Etc/GMT+0', 'Etc/GMT+0'), ('Europe/Vilnius', 'Europe/Vilnius'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('America/Asuncion', 'America/Asuncion'), ('America/Mazatlan', 'America/Mazatlan'), ('Asia/Istanbul', 'Asia/Istanbul'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('Asia/Katmandu', 'Asia/Katmandu'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Etc/GMT-5', 'Etc/GMT-5'), ('Asia/Hebron', 'Asia/Hebron'), ('US/Aleutian', 'US/Aleutian'), ('Africa/Kigali', 'Africa/Kigali'), ('Asia/Jakarta', 'Asia/Jakarta'), ('Europe/Moscow', 'Europe/Moscow'), ('Indian/Mayotte', 'Indian/Mayotte'), ('America/Virgin', 'America/Virgin'), ('America/Boise', 'America/Boise'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('Pacific/Wake', 'Pacific/Wake'), ('Asia/Barnaul', 'Asia/Barnaul'), ('Etc/GMT-10', 'Etc/GMT-10'), ('Asia/Yangon', 'Asia/Yangon'), ('Asia/Bahrain', 'Asia/Bahrain'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('America/Santarem', 'America/Santarem'), ('America/Thule', 'America/Thule'), ('ROC', 'ROC'), ('America/Atka', 'America/Atka'), ('Asia/Rangoon', 'Asia/Rangoon'), ('Europe/Malta', 'Europe/Malta'), ('Etc/GMT+3', 'Etc/GMT+3'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Africa/Tunis', 'Africa/Tunis'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('Africa/Windhoek', 'Africa/Windhoek'), ('Africa/Asmera', 'Africa/Asmera'), ('Africa/Casablanca', 'Africa/Casablanca'), ('America/Regina', 'America/Regina'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Europe/Saratov', 'Europe/Saratov'), ('Asia/Beirut', 'Asia/Beirut'), ('America/Toronto', 'America/Toronto'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('MST', 'MST'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('US/Pacific', 'US/Pacific'), ('Asia/Macau', 'Asia/Macau'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Asia/Kuching', 'Asia/Kuching'), ('Etc/GMT-4', 'Etc/GMT-4'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Pacific/Chatham', 'Pacific/Chatham'), ('Indian/Cocos', 'Indian/Cocos'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('Europe/Monaco', 'Europe/Monaco'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('America/Rainy_River', 'America/Rainy_River'), ('Asia/Brunei', 'Asia/Brunei'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('America/Porto_Acre', 'America/Porto_Acre'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('America/Costa_Rica', 'America/Costa_Rica'), ('Asia/Magadan', 'Asia/Magadan'), ('Africa/Nairobi', 'Africa/Nairobi'), ('Etc/GMT-11', 'Etc/GMT-11'), ('Europe/Brussels', 'Europe/Brussels'), ('Australia/Darwin', 'Australia/Darwin'), ('Europe/Dublin', 'Europe/Dublin'), ('Africa/Tripoli', 'Africa/Tripoli'), ('Pacific/Midway', 'Pacific/Midway'), ('Asia/Kashgar', 'Asia/Kashgar'), ('Africa/Lagos', 'Africa/Lagos'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('America/Rio_Branco', 'America/Rio_Branco'), ('Africa/Banjul', 'Africa/Banjul'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('Europe/Nicosia', 'Europe/Nicosia'), ('UTC', 'UTC'), ('Europe/Helsinki', 'Europe/Helsinki'), ('build/etc/localtime', 'build/etc/localtime'), ('America/La_Paz', 'America/La_Paz'), ('HST', 'HST'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('Africa/Mbabane', 'Africa/Mbabane'), ('America/Goose_Bay', 'America/Goose_Bay'), ('Asia/Dacca', 'Asia/Dacca'), ('Asia/Oral', 'Asia/Oral'), ('America/Metlakatla', 'America/Metlakatla'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('America/Bogota', 'America/Bogota'), ('Etc/GMT+11', 'Etc/GMT+11'), ('Europe/Jersey', 'Europe/Jersey'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('EST', 'EST'), ('America/Grand_Turk', 'America/Grand_Turk'), ('America/New_York', 'America/New_York'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('America/Araguaina', 'America/Araguaina'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Etc/GMT+8', 'Etc/GMT+8'), ('Etc/GMT-6', 'Etc/GMT-6'), ('Africa/Ceuta', 'Africa/Ceuta'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Pacific/Niue', 'Pacific/Niue'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('America/Nassau', 'America/Nassau'), ('America/Chicago', 'America/Chicago'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('America/Matamoros', 'America/Matamoros'), ('Indian/Mahe', 'Indian/Mahe'), ('America/Cordoba', 'America/Cordoba'), ('Asia/Qostanay', 'Asia/Qostanay'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('Europe/Kirov', 'Europe/Kirov'), ('Africa/Harare', 'Africa/Harare'), ('Asia/Tokyo', 'Asia/Tokyo'), ('Asia/Tomsk', 'Asia/Tomsk'), ('Japan', 'Japan'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('Australia/South', 'Australia/South'), ('Etc/UCT', 'Etc/UCT'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('America/Guayaquil', 'America/Guayaquil'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Europe/Kiev', 'Europe/Kiev'), ('Pacific/Noumea', 'Pacific/Noumea'), ('Canada/Atlantic', 'Canada/Atlantic'), ('Europe/Oslo', 'Europe/Oslo'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('America/Dominica', 'America/Dominica'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('Asia/Hovd', 'Asia/Hovd'), ('Etc/GMT-0', 'Etc/GMT-0'), ('Pacific/Samoa', 'Pacific/Samoa'), ('Kwajalein', 'Kwajalein'), ('MET', 'MET'), ('Asia/Chungking', 'Asia/Chungking'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('Etc/GMT-9', 'Etc/GMT-9'), ('Asia/Kabul', 'Asia/Kabul'), ('GB', 'GB'), ('America/Cancun', 'America/Cancun'), ('NZ', 'NZ'), ('Europe/Kyiv', 'Europe/Kyiv'), ('Asia/Manila', 'Asia/Manila'), ('Australia/LHI', 'Australia/LHI'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('America/Lima', 'America/Lima'), ('America/Maceio', 'America/Maceio'), ('Brazil/West', 'Brazil/West'), ('Etc/GMT0', 'Etc/GMT0'), ('Factory', 'Factory'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('Brazil/Acre', 'Brazil/Acre'), ('America/Manaus', 'America/Manaus'), ('Hongkong', 'Hongkong'), ('America/Barbados', 'America/Barbados'), ('Canada/Mountain', 'Canada/Mountain'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('America/Aruba', 'America/Aruba'), ('Africa/Malabo', 'Africa/Malabo'), ('Asia/Thimbu', 'Asia/Thimbu'), ('America/Panama', 'America/Panama'), ('Asia/Aden', 'Asia/Aden')], default='Europe/London', max_length=35),
        ),
    ]
