from datetime import datetime as dt
from json import JSONEncoder
from pathlib import Path


def __converter(self, obj):
    if (class_json_method := getattr(obj.__class__, "__json__", None)) is not None:
        return class_json_method(obj)
    if isinstance(obj, Path | dt):
        return str(obj)
    return __converter.default(obj)


__converter.default = JSONEncoder().default
JSONEncoder.default = __converter
