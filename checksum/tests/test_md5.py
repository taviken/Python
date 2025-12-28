from ..md5 import md5, checkdir
from pathlib import Path

_this_dir = Path(__file__).parent
_dummy_payload = _this_dir / "dummy_payload.txt"
_dummy_dir = _this_dir / "dummy_dir"


def test_md5():
    hashed = md5(_dummy_payload)
    assert hashed == "3858f62230ac3c915f300c664312c63f"


def test_check_dir():
    checksum = checkdir(_dummy_dir)
    assert checksum == "7813987d9dc87851f49ecbed9f875968"
