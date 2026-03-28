import json
from pathlib import Path
from typing import Any, TypeAlias


JSON: TypeAlias = dict[str, Any] | list


def readJSON(filepath: Path) -> JSON:
    if not filepath.suffix == ".json":
        raise RuntimeError(f"JSON Helper: File '{filepath}' is not a JSON file")
    if not filepath.is_file():
        raise RuntimeError(f"JSON Helper: File '{filepath}' does not exist")
    with open(filepath, mode="rt", newline="\n") as jsonfile:
        contents: JSON = json.load(jsonfile)
    return contents


def writeJSON(filepath: Path, contents: JSON, *, sort: bool = False) -> None:
    if not isinstance(contents, dict | list):
        raise RuntimeError(f"JSON Helper: Expected: '{JSON}' to write, got: {type(contents)}")
    with open(filepath, mode="wt", newline="\n") as jsonfile:
        jsonfile.write(json.dumps(contents, ensure_ascii=False, indent=2, sort_keys=sort))


def toReadableJSON(contents: dict | list, *, sort: bool = False) -> str:
    return json.dumps(contents, ensure_ascii=False, indent=2, sort_keys=sort)
