from django.conf import settings

# https://justforex.com/education/currencies
ALL_CURRENCY_CODES = getattr(settings, 'ALL_CURRENCY_CODES', [
    'AED', 'AFN', 'ALL', 'AMD', 'AOA', 'ARS',
    'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT',
    'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB',
    'BRL', 'BSD', 'BTN', 'BWP', 'BYR', 'BZD',
    'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP',
    'CRC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK',
    'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR',
    'FJD', 'FKP', 'GBP', 'GEL', 'GHS', 'GIP',
    'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL',
    'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'INR',
    'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'JPY',
    'KES', 'KGS', 'KHR', 'KPW', 'KRW', 'KWD',
    'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD',
    'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD',
    'MMK', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR',
    'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN',
    'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB',
    'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG',
    'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR',
    'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP',
    'SLL', 'SOS', 'SRD', 'STD', 'SYP', 'SZL',
    'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY',
    'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD',
    'UYU', 'UZS', 'VEF', 'VND', 'VUV', 'WST',
    'XAF', 'XCD', 'XPF', 'YER', 'ZAR', 'ZMW',
])

PRIORITY_CURRENCY_CODES = getattr(settings, 'PRIORITY_CURRENCY_CODES', [])

ALL_CURRENCY_INFO = [
  {
    "code": "AED",
    "country": ["AE"],
    "name": "UAE Dirham",
    "number": 784,
    "symbol": "د.إ"
  },
  {
    "code": "AFN",
    "country": ["AF"],
    "name": "Afghani",
    "number": 971,
    "symbol": "Af"
  },
  { "code": "ALL", "country": ["AL"], "name": "Lek", "number": 8, "symbol": "L" },
  {
    "code": "AMD",
    "country": ["AM"],
    "name": "Armenian Dram",
    "number": 51,
    "symbol": "Դ"
  },
  {
    "code": "AOA",
    "country": ["AO"],
    "name": "Kwanza",
    "number": 973,
    "symbol": "Kz"
  },
  {
    "code": "ARS",
    "country": ["AR"],
    "name": "Argentine Peso",
    "number": 32,
    "symbol": "$"
  },
  {
    "code": "AUD",
    "country": ["AU", "CC", "CX", "HM", "KI", "NF", "NR", "TV"],
    "name": "Australian Dollar",
    "number": 36,
    "symbol": "$"
  },
  {
    "code": "AWG",
    "country": ["AW"],
    "name": "Aruban Guilder/Florin",
    "number": 533,
    "symbol": "ƒ"
  },
  {
    "code": "AZN",
    "country": ["AZ"],
    "name": "Azerbaijanian Manat",
    "number": 944,
    "symbol": "ман"
  },
  {
    "code": "BAM",
    "country": ["BA"],
    "name": "Konvertibilna Marka",
    "number": 977,
    "symbol": "КМ"
  },
  {
    "code": "BBD",
    "country": ["BB"],
    "name": "Barbados Dollar",
    "number": 52,
    "symbol": "$"
  },
  {
    "code": "BDT",
    "country": ["BD"],
    "name": "Taka",
    "number": 50,
    "symbol": "৳"
  },
  {
    "code": "BGN",
    "country": ["BG"],
    "name": "Bulgarian Lev",
    "number": 975,
    "symbol": "лв"
  },
  {
    "code": "BHD",
    "country": ["BH"],
    "name": "Bahraini Dinar",
    "number": 48,
    "symbol": "ب.د"
  },
  {
    "code": "BIF",
    "country": ["BI"],
    "name": "Burundi Franc",
    "number": 108,
    "symbol": "₣"
  },
  {
    "code": "BMD",
    "country": ["BM"],
    "name": "Bermudian Dollar",
    "number": 60,
    "symbol": "$"
  },
  {
    "code": "BND",
    "country": ["BN"],
    "name": "Brunei Dollar",
    "number": 96,
    "symbol": "$"
  },
  {
    "code": "BOB",
    "country": ["BO"],
    "name": "Boliviano",
    "number": 68,
    "symbol": "Bs."
  },
  {
    "code": "BRL",
    "country": ["BR"],
    "name": "Brazilian Real",
    "number": 986,
    "symbol": "R$"
  },
  {
    "code": "BSD",
    "country": ["BS"],
    "name": "Bahamian Dollar",
    "number": 44,
    "symbol": "$"
  },
  {
    "code": "BTN",
    "country": ["BT"],
    "name": "Ngultrum",
    "number": 64,
    "symbol": ""
  },
  {
    "code": "BWP",
    "country": ["BW"],
    "name": "Pula",
    "number": 72,
    "symbol": "P"
  },
  {
    "code": "BYR",
    "country": ["BY"],
    "name": "Belarussian Ruble",
    "number": 974,
    "symbol": "Br"
  },
  {
    "code": "BZD",
    "country": ["BZ"],
    "name": "Belize Dollar",
    "number": 84,
    "symbol": "$"
  },
  {
    "code": "CAD",
    "country": ["CA"],
    "name": "Canadian Dollar",
    "number": 124,
    "symbol": "$"
  },
  {
    "code": "CDF",
    "country": ["CD"],
    "name": "Congolese Franc",
    "number": 976,
    "symbol": "₣"
  },
  {
    "code": "CHF",
    "country": ["CH", "LI"],
    "name": "Swiss Franc",
    "number": 756,
    "symbol": "₣"
  },
  {
    "code": "CLP",
    "country": ["CL"],
    "name": "Chilean Peso",
    "number": 152,
    "symbol": "$"
  },
  {
    "code": "CNY",
    "country": ["CN"],
    "name": "Yuan",
    "number": 156,
    "symbol": "¥"
  },
  {
    "code": "COP",
    "country": ["CO"],
    "name": "Colombian Peso",
    "number": 170,
    "symbol": "$"
  },
  {
    "code": "CRC",
    "country": ["CR"],
    "name": "Costa Rican Colon",
    "number": 188,
    "symbol": "₡"
  },
  {
    "code": "CUP",
    "country": ["CU"],
    "name": "Cuban Peso",
    "number": 192,
    "symbol": "$"
  },
  {
    "code": "CVE",
    "country": ["CV"],
    "name": "Cape Verde Escudo",
    "number": 132,
    "symbol": "$"
  },
  {
    "code": "CZK",
    "country": ["CZ"],
    "name": "Czech Koruna",
    "number": 203,
    "symbol": "Kč"
  },
  {
    "code": "DJF",
    "country": ["DJ"],
    "name": "Djibouti Franc",
    "number": 262,
    "symbol": "₣"
  },
  {
    "code": "DKK",
    "country": ["DK", "FO", "GL"],
    "name": "Danish Krone",
    "number": 208,
    "symbol": "kr"
  },
  {
    "code": "DOP",
    "country": ["DO"],
    "name": "Dominican Peso",
    "number": 214,
    "symbol": "$"
  },
  {
    "code": "DZD",
    "country": ["DZ"],
    "name": "Algerian Dinar",
    "number": 12,
    "symbol": "د.ج"
  },
  {
    "code": "EGP",
    "country": ["EG"],
    "name": "Egyptian Pound",
    "number": 818,
    "symbol": "£"
  },
  {
    "code": "ERN",
    "country": ["ER"],
    "name": "Nakfa",
    "number": 232,
    "symbol": "Nfk"
  },
  {
    "code": "ETB",
    "country": ["ET"],
    "name": "Ethiopian Birr",
    "number": 230,
    "symbol": ""
  },
  {
    "code": "EUR",
    "country": [
      "AD",
      "AT",
      "AX",
      "BE",
      "BL",
      "CY",
      "DE",
      "EE",
      "ES",
      "FI",
      "FR",
      "GF",
      "GP",
      "GR",
      "IE",
      "IT",
      "LT",
      "LU",
      "LV",
      "MC",
      "ME",
      "MF",
      "MQ",
      "MT",
      "NL",
      "PM",
      "PT",
      "RE",
      "SI",
      "SK",
      "SM",
      "TF",
      "VA",
      "YT"
    ],
    "name": "Euro",
    "number": 978,
    "symbol": "€"
  },
  {
    "code": "FJD",
    "country": ["FJ"],
    "name": "Fiji Dollar",
    "number": 242,
    "symbol": "$"
  },
  {
    "code": "FKP",
    "country": ["FK"],
    "name": "Falkland Islands Pound",
    "number": 238,
    "symbol": "£"
  },
  {
    "code": "GBP",
    "country": ["GB", "GG", "IM", "JE"],
    "name": "Pound Sterling",
    "number": 826,
    "symbol": "£"
  },
  {
    "code": "GEL",
    "country": ["GE"],
    "name": "Lari",
    "number": 981,
    "symbol": "ლ"
  },
  {
    "code": "GHS",
    "country": ["GH"],
    "name": "Cedi",
    "number": 936,
    "symbol": "₵"
  },
  {
    "code": "GIP",
    "country": ["GI"],
    "name": "Gibraltar Pound",
    "number": 292,
    "symbol": "£"
  },
  {
    "code": "GMD",
    "country": ["GM"],
    "name": "Dalasi",
    "number": 270,
    "symbol": "D"
  },
  {
    "code": "GNF",
    "country": ["GN"],
    "name": "Guinea Franc",
    "number": 324,
    "symbol": "₣"
  },
  {
    "code": "GTQ",
    "country": ["GT"],
    "name": "Quetzal",
    "number": 320,
    "symbol": "Q"
  },
  {
    "code": "GYD",
    "country": ["GY"],
    "name": "Guyana Dollar",
    "number": 328,
    "symbol": "$"
  },
  {
    "code": "HKD",
    "country": ["HK"],
    "name": "Hong Kong Dollar",
    "number": 344,
    "symbol": "$"
  },
  {
    "code": "HNL",
    "country": ["HN"],
    "name": "Lempira",
    "number": 340,
    "symbol": "L"
  },
  {
    "code": "HRK",
    "country": ["HR"],
    "name": "Croatian Kuna",
    "number": 191,
    "symbol": "Kn"
  },
  {
    "code": "HTG",
    "country": ["HT"],
    "name": "Gourde",
    "number": 332,
    "symbol": "G"
  },
  {
    "code": "HUF",
    "country": ["HU"],
    "name": "Forint",
    "number": 348,
    "symbol": "Ft"
  },
  {
    "code": "IDR",
    "country": ["ID"],
    "name": "Rupiah",
    "number": 360,
    "symbol": "Rp"
  },
  {
    "code": "ILS",
    "country": ["IL"],
    "name": "New Israeli Shekel",
    "number": 376,
    "symbol": "₪"
  },
  {
    "code": "INR",
    "country": ["BT", "IN"],
    "name": "Indian Rupee",
    "number": 356,
    "symbol": "₨"
  },
  {
    "code": "IQD",
    "country": ["IQ"],
    "name": "Iraqi Dinar",
    "number": 368,
    "symbol": "ع.د"
  },
  {
    "code": "IRR",
    "country": ["IR"],
    "name": "Iranian Rial",
    "number": 364,
    "symbol": "﷼"
  },
  {
    "code": "ISK",
    "country": ["IS"],
    "name": "Iceland Krona",
    "number": 352,
    "symbol": "Kr"
  },
  {
    "code": "JMD",
    "country": ["JM"],
    "name": "Jamaican Dollar",
    "number": 388,
    "symbol": "$"
  },
  {
    "code": "JOD",
    "country": ["JO"],
    "name": "Jordanian Dinar",
    "number": 400,
    "symbol": "د.ا"
  },
  {
    "code": "JPY",
    "country": ["JP"],
    "name": "Yen",
    "number": 392,
    "symbol": "¥"
  },
  {
    "code": "KES",
    "country": ["KE"],
    "name": "Kenyan Shilling",
    "number": 404,
    "symbol": "Sh"
  },
  { "code": "KGS", "country": ["KG"], "name": "Som", "number": 417, "symbol": "" },
  {
    "code": "KHR",
    "country": ["KH"],
    "name": "Riel",
    "number": 116,
    "symbol": "៛"
  },
  {
    "code": "KPW",
    "country": ["KP"],
    "name": "North Korean Won",
    "number": 408,
    "symbol": "₩"
  },
  {
    "code": "KRW",
    "country": ["KR"],
    "name": "South Korean Won",
    "number": 410,
    "symbol": "₩"
  },
  {
    "code": "KWD",
    "country": ["KW"],
    "name": "Kuwaiti Dinar",
    "number": 414,
    "symbol": "د.ك"
  },
  {
    "code": "KYD",
    "country": ["KY"],
    "name": "Cayman Islands Dollar",
    "number": 136,
    "symbol": "$"
  },
  {
    "code": "KZT",
    "country": ["KZ"],
    "name": "Tenge",
    "number": 398,
    "symbol": "〒"
  },
  {
    "code": "LAK",
    "country": ["LA"],
    "name": "Kip",
    "number": 418,
    "symbol": "₭"
  },
  {
    "code": "LBP",
    "country": ["LB"],
    "name": "Lebanese Pound",
    "number": 422,
    "symbol": "ل.ل"
  },
  {
    "code": "LKR",
    "country": ["LK"],
    "name": "Sri Lanka Rupee",
    "number": 144,
    "symbol": "Rs"
  },
  {
    "code": "LRD",
    "country": ["LR"],
    "name": "Liberian Dollar",
    "number": 430,
    "symbol": "$"
  },
  {
    "code": "LSL",
    "country": ["LS"],
    "name": "Loti",
    "number": 426,
    "symbol": "L"
  },
  {
    "code": "LYD",
    "country": ["LY"],
    "name": "Libyan Dinar",
    "number": 434,
    "symbol": "ل.د"
  },
  {
    "code": "MAD",
    "country": ["EH", "MA"],
    "name": "Moroccan Dirham",
    "number": 504,
    "symbol": "د.م."
  },
  {
    "code": "MDL",
    "country": ["MD"],
    "name": "Moldavian Leu",
    "number": 498,
    "symbol": "L"
  },
  {
    "code": "MGA",
    "country": ["MG"],
    "name": "Malagasy Ariary",
    "number": 969,
    "symbol": ""
  },
  {
    "code": "MKD",
    "country": ["MK"],
    "name": "Denar",
    "number": 807,
    "symbol": "ден"
  },
  {
    "code": "MMK",
    "country": ["MM"],
    "name": "Kyat",
    "number": 104,
    "symbol": "K"
  },
  {
    "code": "MNT",
    "country": ["MN"],
    "name": "Tugrik",
    "number": 496,
    "symbol": "₮"
  },
  {
    "code": "MOP",
    "country": ["MO"],
    "name": "Pataca",
    "number": 446,
    "symbol": "P"
  },
  {
    "code": "MRO",
    "country": ["MR"],
    "name": "Ouguiya",
    "number": 478,
    "symbol": "UM"
  },
  {
    "code": "MUR",
    "country": ["MU"],
    "name": "Mauritius Rupee",
    "number": 480,
    "symbol": "₨"
  },
  {
    "code": "MVR",
    "country": ["MV"],
    "name": "Rufiyaa",
    "number": 462,
    "symbol": "ރ."
  },
  {
    "code": "MWK",
    "country": ["MW"],
    "name": "Kwacha",
    "number": 454,
    "symbol": "MK"
  },
  {
    "code": "MXN",
    "country": ["MX"],
    "name": "Mexican Peso",
    "number": 484,
    "symbol": "$"
  },
  {
    "code": "MYR",
    "country": ["MY"],
    "name": "Malaysian Ringgit",
    "number": 458,
    "symbol": "RM"
  },
  {
    "code": "MZN",
    "country": ["MZ"],
    "name": "Metical",
    "number": 943,
    "symbol": "MTn"
  },
  {
    "code": "NAD",
    "country": ["NA"],
    "name": "Namibia Dollar",
    "number": 516,
    "symbol": "$"
  },
  {
    "code": "NGN",
    "country": ["NG"],
    "name": "Naira",
    "number": 566,
    "symbol": "₦"
  },
  {
    "code": "NIO",
    "country": ["NI"],
    "name": "Cordoba Oro",
    "number": 558,
    "symbol": "C$"
  },
  {
    "code": "NOK",
    "country": ["BV", "NO", "SJ"],
    "name": "Norwegian Krone",
    "number": 578,
    "symbol": "kr"
  },
  {
    "code": "NPR",
    "country": ["NP"],
    "name": "Nepalese Rupee",
    "number": 524,
    "symbol": "₨"
  },
  {
    "code": "NZD",
    "country": ["CK", "NU", "NZ", "PN", "TK"],
    "name": "New Zealand Dollar",
    "number": 554,
    "symbol": "$"
  },
  {
    "code": "OMR",
    "country": ["OM"],
    "name": "Rial Omani",
    "number": 512,
    "symbol": "ر.ع."
  },
  {
    "code": "PAB",
    "country": ["PA"],
    "name": "Balboa",
    "number": 590,
    "symbol": "B/."
  },
  {
    "code": "PEN",
    "country": ["PE"],
    "name": "Nuevo Sol",
    "number": 604,
    "symbol": "S/."
  },
  {
    "code": "PGK",
    "country": ["PG"],
    "name": "Kina",
    "number": 598,
    "symbol": "K"
  },
  {
    "code": "PHP",
    "country": ["PH"],
    "name": "Philippine Peso",
    "number": 608,
    "symbol": "₱"
  },
  {
    "code": "PKR",
    "country": ["PK"],
    "name": "Pakistan Rupee",
    "number": 586,
    "symbol": "₨"
  },
  {
    "code": "PLN",
    "country": ["PL"],
    "name": "PZloty",
    "number": 985,
    "symbol": "zł"
  },
  {
    "code": "PYG",
    "country": ["PY"],
    "name": "Guarani",
    "number": 600,
    "symbol": "₲"
  },
  {
    "code": "QAR",
    "country": ["QA"],
    "name": "Qatari Rial",
    "number": 634,
    "symbol": "ر.ق"
  },
  {
    "code": "RON",
    "country": ["RO"],
    "name": "Leu",
    "number": 946,
    "symbol": "L"
  },
  {
    "code": "RSD",
    "country": ["RS"],
    "name": "Serbian Dinar",
    "number": 941,
    "symbol": "din"
  },
  {
    "code": "RUB",
    "country": ["RU"],
    "name": "Russian Ruble",
    "number": 643,
    "symbol": "р."
  },
  {
    "code": "RWF",
    "country": ["RW"],
    "name": "Rwanda Franc",
    "number": 646,
    "symbol": "₣"
  },
  {
    "code": "SAR",
    "country": ["SA"],
    "name": "Saudi Riyal",
    "number": 682,
    "symbol": "ر.س"
  },
  {
    "code": "SBD",
    "country": ["SB"],
    "name": "Solomon Islands Dollar",
    "number": 90,
    "symbol": "$"
  },
  {
    "code": "SCR",
    "country": ["SC"],
    "name": "Seychelles Rupee",
    "number": 690,
    "symbol": "₨"
  },
  {
    "code": "SDG",
    "country": ["SD"],
    "name": "Sudanese Pound",
    "number": 938,
    "symbol": "£"
  },
  {
    "code": "SEK",
    "country": ["SE"],
    "name": "Swedish Krona",
    "number": 752,
    "symbol": "kr"
  },
  {
    "code": "SGD",
    "country": ["SG"],
    "name": "Singapore Dollar",
    "number": 702,
    "symbol": "$"
  },
  {
    "code": "SHP",
    "country": ["SH"],
    "name": "Saint Helena Pound",
    "number": 654,
    "symbol": "£"
  },
  {
    "code": "SLL",
    "country": ["SL"],
    "name": "Leone",
    "number": 694,
    "symbol": "Le"
  },
  {
    "code": "SOS",
    "country": ["SO"],
    "name": "Somali Shilling",
    "number": 706,
    "symbol": "Sh"
  },
  {
    "code": "SRD",
    "country": ["SR"],
    "name": "Suriname Dollar",
    "number": 968,
    "symbol": "$"
  },
  {
    "code": "STD",
    "country": ["ST"],
    "name": "Dobra",
    "number": 678,
    "symbol": "Db"
  },
  {
    "code": "SYP",
    "country": ["SY"],
    "name": "Syrian Pound",
    "number": 760,
    "symbol": "ل.س"
  },
  {
    "code": "SZL",
    "country": ["SZ"],
    "name": "Lilangeni",
    "number": 748,
    "symbol": "L"
  },
  {
    "code": "THB",
    "country": ["TH"],
    "name": "Baht",
    "number": 764,
    "symbol": "฿"
  },
  {
    "code": "TJS",
    "country": ["TJ"],
    "name": "Somoni",
    "number": 972,
    "symbol": "ЅМ"
  },
  {
    "code": "TMT",
    "country": ["TM"],
    "name": "Manat",
    "number": 934,
    "symbol": "m"
  },
  {
    "code": "TND",
    "country": ["TN"],
    "name": "Tunisian Dinar",
    "number": 788,
    "symbol": "د.ت"
  },
  {
    "code": "TOP",
    "country": ["TO"],
    "name": "Pa’anga",
    "number": 776,
    "symbol": "T$"
  },
  {
    "code": "TRY",
    "country": ["TR"],
    "name": "Turkish Lira",
    "number": 949,
    "symbol": "₤"
  },
  {
    "code": "TTD",
    "country": ["TT"],
    "name": "Trinidad and Tobago Dollar",
    "number": 780,
    "symbol": "$"
  },
  {
    "code": "TWD",
    "country": ["TW"],
    "name": "Taiwan Dollar",
    "number": 901,
    "symbol": "$"
  },
  {
    "code": "TZS",
    "country": ["TZ"],
    "name": "Tanzanian Shilling",
    "number": 834,
    "symbol": "Sh"
  },
  {
    "code": "UAH",
    "country": ["UA"],
    "name": "Hryvnia",
    "number": 980,
    "symbol": "₴"
  },
  {
    "code": "UGX",
    "country": ["UG"],
    "name": "Uganda Shilling",
    "number": 800,
    "symbol": "Sh"
  },
  {
    "code": "USD",
    "country": [
      "AS",
      "BQ",
      "EC",
      "FM",
      "GU",
      "HT",
      "IO",
      "MH",
      "MP",
      "PA",
      "PR",
      "PW",
      "SV",
      "TC",
      "TL",
      "UM",
      "US",
      "VG",
      "VI"
    ],
    "name": "US Dollar",
    "number": 840,
    "symbol": "$"
  },
  {
    "code": "UYU",
    "country": ["UY"],
    "name": "Peso Uruguayo",
    "number": 858,
    "symbol": "$"
  },
  {
    "code": "UZS",
    "country": ["UZ"],
    "name": "Uzbekistan Sum",
    "number": 860,
    "symbol": ""
  },
  {
    "code": "VEF",
    "country": ["VE"],
    "name": "Bolivar Fuerte",
    "number": 937,
    "symbol": "Bs F"
  },
  {
    "code": "VND",
    "country": ["VN"],
    "name": "Dong",
    "number": 704,
    "symbol": "₫"
  },
  {
    "code": "VUV",
    "country": ["VU"],
    "name": "Vatu",
    "number": 548,
    "symbol": "Vt"
  },
  {
    "code": "WST",
    "country": ["WS"],
    "name": "Tala",
    "number": 882,
    "symbol": "T"
  },
  {
    "code": "XAF",
    "country": ["CF", "CG", "CM", "GA", "GQ", "TD"],
    "name": "CFA Franc BCEAO",
    "number": 950,
    "symbol": "₣"
  },
  {
    "code": "XCD",
    "country": ["AG", "AI", "DM", "GD", "KN", "LC", "MS", "VC"],
    "name": "East Caribbean Dollar",
    "number": 951,
    "symbol": "$"
  },
  {
    "code": "XPF",
    "country": ["NC", "PF", "WF"],
    "name": "CFP Franc",
    "number": 953,
    "symbol": "₣"
  },
  {
    "code": "YER",
    "country": ["YE"],
    "name": "Yemeni Rial",
    "number": 886,
    "symbol": "﷼"
  },
  {
    "code": "ZAR",
    "country": ["LS", "NA", "ZA"],
    "name": "Rand",
    "number": 710,
    "symbol": "R"
  },
  {
    "code": "ZMW",
    "country": ["ZM"],
    "name": "Zambian Kwacha",
    "number": 967,
    "symbol": "ZK"
  },
  {
    "code": "ZWL",
    "country": ["ZW"],
    "name": "Zimbabwe Dollar",
    "number": 932,
    "symbol": "$"
  }
]
