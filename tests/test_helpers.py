from pathlib import Path
from typing import Any

from kaktus.json_helpers.helpers import JSON, readJSON, writeJSON


def test_write_and_read_json_roundtrip(tmp_path: Path) -> None:
    filepath: Path = tmp_path / "sample.json"
    payload: dict[str, Any] = {
        "name": "kaktus",
        "items": [1, 2, 3],
        "nested": {"ok": True},
    }

    writeJSON(filepath, payload)
    assert filepath.is_file()

    loaded: JSON = readJSON(filepath)
    assert loaded == payload


def test_write_json_with_sort(tmp_path: Path) -> None:
    filepath: Path = tmp_path / "sorted.json"
    writeJSON(filepath, {"b": 2, "a": 1}, sort=True)

    assert filepath.read_text(encoding="utf-8") == '{\n  "a": 1,\n  "b": 2\n}'
