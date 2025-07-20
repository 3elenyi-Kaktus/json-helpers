import json
from pathlib import Path
from typing import Any


class JSONManager:
    @staticmethod
    def isJSONFile(filepath: Path) -> bool:
        return filepath.suffix == ".json"

    def readJSON(self, filepath: Path) -> Any:
        if not self.isJSONFile(filepath):
            raise RuntimeError(f"JSONManager: File '{filepath}' is not a JSON file")
        if not filepath.is_file():
            raise RuntimeError(f"JSONManager: File '{filepath}' does not exist")
        with open(filepath, mode="rt", newline="\n") as jsonfile:
            contents: Any = json.load(jsonfile)
        return contents

    @staticmethod
    def writeJSON(filepath: Path, contents: dict | list) -> None:
        if not isinstance(contents, dict | list):
            raise RuntimeError(f"JSONManager: Expected dict or list to write, got '{type(contents)}'")
        with open(filepath, mode="wt", newline="\n") as jsonfile:
            jsonfile.write(json.dumps(contents, ensure_ascii=False, indent=4, sort_keys=True))

    @staticmethod
    def toReadableJSON(contents: dict | list) -> str:
        return json.dumps(contents, ensure_ascii=False, indent=4, sort_keys=True)


toReadableJSON = JSONManager.toReadableJSON
