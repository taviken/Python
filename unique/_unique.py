"""Module that contains recipes for unique classes"""


class UniqueValueError(ValueError):
    """'Uniuq Subclass of ValueError"""


def make_unique(*, key):
    """Creates a metaclass with the uniquness pattern based on a given key"""
    class MetaUnique(type):
        """MetaUnique metaclass"""
        # _req_key = key
        # _instances = {}
        _ids = set()

        def __new__(mcs, *args, **kwargs):

            _, _, dict_ = args
            annotations = dict_.get('__annotations__')
            if annotations is None:
                raise UniqueValueError(
                    f"{mcs.__class__.__name__} must have '{key}' annotations")
            # if key in annotations:
            #     raise UniqueValueError(f"{key} already taken")
            inst = super().__new__(mcs, *args, **kwargs)

            return inst

        def __call__(cls, *args, **kwargs):
            inst = super().__call__(*args, **kwargs)
            attr = getattr(inst, key)
            if attr in MetaUnique._ids:
                raise UniqueValueError(f"'{attr}' already taken")
            MetaUnique._ids.add(attr)
            return inst

    return MetaUnique
