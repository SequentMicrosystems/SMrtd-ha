import librtd
API = librtd
DOMAIN = "SMrtd"
NAME_PREFIX = "smrtd"
SM_MAP = {
    "sensor":  {
        "rtd": {
                "chan_no": 8,
                "uom": "°C",
                "com": {
                    "get": "get",
                },
        },
        "res": {
                "chan_no": 8,
                "uom": "Ohm",
                "com": {
                    "get": "getRes",
                },
        },
        "poly5": {
                "chan_no": 8,
                "uom": "°C",
                "com": {
                    "get": "get_poly5",
                },
        },
    },
}
