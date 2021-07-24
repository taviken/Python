from cryptography.hazmat.primitives.asymmetric import rsa


class KeyPair:
    def __init__(self):
        self._private = rsa.generate_private_key((65537, 2048))

    @property
    def public_key(self):
        publicObj = self._private.public_key()
        pubnums = publicObj.public_numbers()
        return pubnums.n


class Wallet:
    def __init__(self):
        self._balance = 0.0
        self._privateKey = KeyPair()

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value: float):
        self._balance = float(value)

    @property
    def publicKey(self):
        return self._privateKey.public_key
