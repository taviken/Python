from collections import OrderedDict
from ._block import Block
from typing import Optional
from blockchain import __hasher__


class Chain:

    def __init__(self, blocks: Optional[OrderedDict[str, Block]] = None):
        self.blocks = blocks if blocks is not None else OrderedDict()

    def add_block(self, payload: str, hash_name: str = "sha256") -> None:
        hasher = __hasher__[hash_name]
        linker = Linker(
            payload,
        )
