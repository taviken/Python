from dataclasses import dataclass
from typing import Optional
import random


@dataclass(frozen=True, slots=True)
class Keys:
    """
    Dataclass containg a public and secret key pair
    """

    secret: Optional[int]
    public: Optional[int]


class DiffieHellman:
    """
    This class implements methods relevant to the Diffie-Hellman IKE protocol
    """

    def __init__(self, prime: int, g_root: int) -> None:

        self._prime = prime
        self._g_root = g_root
        self._private = random.SystemRandom().randrange(g_root.bit_count() - 1)
        self.public = self._generate_public_key()
        self._secret: Optional[int] = None

    @property
    def keys(self) -> Keys:
        """
        returns an instance of the dataclass Keys, for this class's internal keys
        """
        return Keys(secret=self._secret, public=self.public)

    @classmethod
    def from_modp(cls, modp):
        return cls(modp.p, modp.g)

    def _generate_public_key(self):
        key = (self._g_root**self._private) % self._prime
        return key

    def generate_secret_key(self, public: int) -> None:
        """
        This method generates the secret Key, based on a given public key
        @parameters:
            public:int - the public key from the corresponding diffie-hellman peer
        @returns:
            None
        """
        self._secret = (public**self._private) % self._prime
