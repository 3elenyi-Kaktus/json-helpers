import subprocess
from subprocess import CompletedProcess
import sys


_PAYLOAD: str = (
    "from datetime import datetime; from pathlib import Path; "
    "data = {'when': datetime(2026, 7, 30), 'where': Path('/tmp/x')}"
)


def test_json_dumps_datetime_and_path_fails_without_make_jsonable() -> None:
    result: CompletedProcess[str] = subprocess.run(
        [
            sys.executable,
            "-c",
            f"import json; {_PAYLOAD}; json.dumps(data)",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode != 0
    assert "TypeError" in result.stderr
    assert "not JSON serializable" in result.stderr


def test_json_dumps_datetime_and_path_works_with_make_jsonable() -> None:
    result: CompletedProcess[str] = subprocess.run(
        [
            sys.executable,
            "-c",
            f"import json; import kaktus.json_helpers.make_jsonable; {_PAYLOAD}; print(json.dumps(data))",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == '{"when": "2026-07-30 00:00:00", "where": "/tmp/x"}'
