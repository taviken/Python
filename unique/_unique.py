"""Module that contains recipes for unique classes"""
def make_unique(*,key):
    class Unique(type):
        _req_key=key
        _ids=set()
        def __call__(cls,*a,**k):
            inst = super().__call__(*a,**k)
            key_ = getattr(inst,key)
            if key_ in Unique._ids:
                raise Exception(f"{key_} already taken")
            Unique._ids.add(key_)
            return inst
    return Unique

class foo(metaclass=make_unique(key='name')):
    def __init__(self, name:str):
        self.name = name