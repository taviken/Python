import struct
from collections import namedtuple


class Field:
    def __init__(self, size: int, data: bytes):
        self.size = size
        self.data = data


class _Word:
    def __init__(self, spec):
        self._spec = spec
        self._masks = {}
        self.__dict__.update(spec)
        self.size = sum(spec.values())
        for key, bit_size in spec.items():
            self._masks[key] = int('1' * bit_size, 2)

    def print(self):
        pos = 0
        for key, bitlength in self._spec.items():
            header = key.ljust(6) + ' : '
            mask = '1' * bitlength
            mask = mask.rjust(pos + bitlength, '-')
            mask = mask.ljust(self.size, '-')
            pos += bitlength
            print(header + mask)


class Word:
    def __repr__(self):
        return self.__class__.__name__


Mask = namedtuple('Mask', ['mask', 'pos'])


def get_data(data, mask: Mask):
    field = data & (mask.mask << mask.pos)
    return field >> mask.pos


def create_word_class(name: str, spec: dict):
    bitpos = 0
    masks = {}
    props = {}
    dict_ = {'wordsize': sum(spec.values()), '_data': 0}
    for field, bitsize in spec.items():
        mask = Mask(int('1' * bitsize, 2), bitpos)
        masks[field] = mask
        props[field] = property(lambda x: get_data(x._data, x._masks[field]))
        bitpos += bitsize
    dict_.update(props)
    dict_['_masks'] = masks
    cls = type(name, (), dict_)
    return cls
