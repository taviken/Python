"""Module that contains recipes for unique classes"""

class UniqueValueError(ValueError):
    """'Uniuq Subclass of ValueError"""


def make_unique(*,key):
    """Creates a metaclass with the uniquness pattern based on a given key"""
    class MetaUnique(type):
        """Unique meta class"""
        _req_key=key
        _ids=set()
        def __call__(cls,*a,**k):
            inst = super().__call__(*a,**k)
            key_ = getattr(inst,key)
            if key_ in MetaUnique._ids:
                raise UniqueValueError(f"{key_} already taken")
            MetaUnique._ids.add(key_)
            return inst

        def __del__(cls):
            key_ = getattr(cls,key)
            if key_ in MetaUnique._ids:
                MetaUnique._ids.discard(cls)
    return MetaUnique

class foo(metaclass=make_unique(key='name')):
    def __init__(self, name:str):
        self.name = name