from dataclasses import dataclass


@dataclass(frozen=True)
class Block:
    digest: str
    nonce: int
    payload: str

    @property
    def encoded(self) -> bytes:
        _format = f"{self.payload}{self.nonce}{self.digest}"
        return _format.encode()
