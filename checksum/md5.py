import hashlib
from pathlib import Path
from typing import Union
import os


def md5(path: Union[Path, str], chunk_size: int = 8192) -> str:
    _md5 = hashlib.md5()
    with open(path, "rb") as fd:
        while chunk := fd.read(chunk_size):
            _md5.update(chunk)
        return _md5.hexdigest()


def checkdir(dir_path: Union[Path, str]):
    _md5 = hashlib.md5()
    hashes = []
    for r, _, files in os.walk(dir_path):
        root = Path(r)
        for file_ in sorted(files):
            f = root / file_
            hashed = md5(f)
            hashes.append(hashed)
    for hash_ in hashes:
        _md5.update(hash_.encode())
    return _md5.hexdigest()


__all__ = [
    "md5",
]
