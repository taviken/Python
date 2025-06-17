from dataclasses import dataclass, field, asdict


@dataclass(frozen=True)
class Block:
    digest: str = field(default_factory=str)
    nonce: int = field(default_factory=int)
    payload: str = field(default_factory=str)

    @property
    def encoded(self) -> bytes:
        _format = f"{self.payload}{self.nonce}{self.digest}"
        return _format.encode()
