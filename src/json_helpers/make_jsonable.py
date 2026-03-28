from datetime import datetime as dt
import json
from json import JSONEncoder
from pathlib import Path
from typing import Any


class ExtendedJSONEncoder(JSONEncoder):
    def default(self, obj: Any) -> Any:
        if (class_json_method := getattr(obj.__class__, "__json__", None)) is not None:
            return class_json_method(obj)
        if isinstance(obj, Path | dt):
            return str(obj)
        return super().default(obj)


json._default_encoder = ExtendedJSONEncoder(
    skipkeys=False,
    ensure_ascii=True,
    check_circular=True,
    allow_nan=True,
    indent=None,
    separators=None,
    default=None,
)
json.JSONEncoder = ExtendedJSONEncoder
