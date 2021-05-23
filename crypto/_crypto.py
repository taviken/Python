import cryptography.hazmat.primitives.asymmetric.rsa as rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import *

_PSS_padding = padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                           salt_length=padding.PSS.MAX_LENGTH)

_OAEP_padding = padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)


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
            _PSS_padding,
            hashes.SHA256()
        )
        return signature

    def verify(self, signature: bytes, message: bytes):
        pub = self._private.public_key()
        verified = True
        try:
            pub.verify(signature, message, _PSS_padding, hashes.SHA256())
        except InvalidSignature:
            verified = False
        return verified

    def encrypt(self, message: bytes):
        pubkey = self._private.public_key()
        return pubkey.encrypt(
            message,
            _OAEP_padding
        )

    def decrypt(self, ciphertext: bytes):
        return self._private.decrypt(
            ciphertext,
            _OAEP_padding
        )
