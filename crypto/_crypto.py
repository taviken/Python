"""This module wraps basic cryptographic functions around the cryptography module"""
import cryptography.hazmat.primitives.asymmetric.rsa as rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import *
from collections import namedtuple

public_key = namedtuple('public_key', ['n', 'e'])

_PSS_padding = padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                           salt_length=padding.PSS.MAX_LENGTH)

_OAEP_padding = padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)


class Crypt:
    def __init__(self):
        self._private = rsa.generate_private_key(65537, 2048)

    @property
    def private_key(self) -> int:
        priv = self._private.private_numbers()
        return priv.d

    @property
    def public_key(self) -> public_key:
        """returns a namedtuple, 'public_key', containing e and n."""
        pub = self._private.public_key()
        pubnum = pub.public_numbers()
        return public_key(n=pubnum.n, e=pubnum.e)

    def sign(self, message: bytes):
        signature = self._private.sign(
            data=message,
            padding=_PSS_padding,
            algorithm=hashes.SHA256()
        )
        return signature

    def verify(self, signature: bytes, message: bytes):
        pub = self._private.public_key()
        verified = True
        try:
            pub.verify(signature=signature,
                       data=message,
                       padding=_PSS_padding,
                       algorithm=hashes.SHA256())
        except InvalidSignature:
            verified = False
        return verified

    def encrypt(self, message: bytes):
        pubkey = self._private.public_key()
        return pubkey.encrypt(
            plaintext=message,
            padding=_OAEP_padding
        )

    def decrypt(self, ciphertext: bytes):
        return self._private.decrypt(
            ciphertext=ciphertext,
            padding=_OAEP_padding
        )
