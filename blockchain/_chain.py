from collections import OrderedDict
from ._block import Block
from typing import Optional
from blockchain import __hasher__, __initial_digest__
from ._link import Linker


class Chain:

    def __init__(self, blocks: Optional[OrderedDict[str, Block]] = None):
        self.blocks = (
            blocks if blocks is not None else OrderedDict(__initial_digest__, Block())
        )

    @property
    def last(self) -> str:
        return next(reversed(self.blocks))

    def add_block(self, payload: str, hash_name: str = "sha256") -> None:
        hasher = __hasher__[hash_name]
        linker = Linker(payload, self.last, hash_name)
