def encrypt(message, key: int) -> bytes:
    return bytearray(a ^ b for a, b in zip(*map(bytearray, [message, key])))
