import numpy as np
from dataclasses import dataclass


def encrypt(message, key: int) -> bytes:
    return bytearray(a ^ b for a, b in zip(*map(bytearray, [message, key])))


block = np.array(
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], dtype=np.uint
)


def chunkit(message: bytes):
    bmessage = [
        bytearray(message[x : x + 16].encode()) for x in range(0, len(message), 16)
    ]
    padding = 16 - (len(message) % 16)
    last_chunk = bytearray(bmessage[-1].decode() + (padding * "0"), "utf-8")
    bmessage[-1] = last_chunk
    return bmessage, padding


@dataclass
class Key:
    array: bytearray

    def __post_init__(self):
        self.array_length = len(self.array)
        self._pos = 0

    def increment(self):
        self._pos += 1
        self._pos %= self.array_length

    def next_byte(self):
        val = self.array[self._pos]
        self.increment()
        return val


def convert_key(key: int) -> Key:
    length = key.bit_length()
    num_bytes = length // 8
    num_bytes += 1 if length % 8 > 0 else 0
    return Key(bytearray(key.to_bytes(num_bytes)))


def cipher(message: bytes, key: int):
    chunked_message, padding = chunkit(message)

    key_ = convert_key(key)
    arrays = []
    for chunk in chunked_message:
        array = bytearray(16)
        for byte in chunk:
            key_byte = key_.next_byte()
            xor = key_byte ^ byte
            array.append(xor)
        arrays.append(array)
    return arrays
