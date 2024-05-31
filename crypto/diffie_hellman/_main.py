from dataclasses import dataclass
from typing import Optional
import random


@dataclass(frozen=True)
class Keys:
    secret: Optional[int]
    public: Optional[int]


class DiffieHellman:
    def __init__(self, prime: int, g_root: int) -> None:
        self.prime = prime
        self.g_root = g_root
        self.private = random.SystemRandom().randrange(g_root.bit_count() - 1)
        self.public = self.generate_public_key()
        self._secret: Optional[int] = None

    @property
    def keys(self) -> Keys:
        return Keys(secret=self._secret, public=self.public)

    @classmethod
    def from_modp(cls, modp):
        return cls(modp.p, modp.g)

    def generate_public_key(self):
        key = (self.g_root**self.private) % self.prime
        return key

    def generate_secret_key(self, public: int):
        self._secret = (public**self.private) % self.prime
