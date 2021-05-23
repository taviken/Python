import cryptography.hazmat.primitives.asymmetric.rsa as rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

_padding = padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                       salt_length=padding.PSS.MAX_LENGTH)

from cryptography.exceptions import *

class Crypt:
    def __init__(self):
        self._private = rsa.generate_private_key(65537, 2048)

    @property
    def public_key(self):
        pub = self._private.public_key()
        pubnum = pub.public_numbers()
        return pubnum.n

    def sign(self, message: bytes):
        signature = self._private.sign(
            message,
            _padding,
            hashes.SHA256()
        )
        return signature

    def verify(self, signature: bytes, message: bytes):
        pub = self._private.public_key()
        verified = True
        try:
            pub.verify(signature, message, _padding, hashes.SHA256())
        except InvalidSignature:
            verified = False
        return verified
