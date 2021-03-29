"""Metaclass demonstration"""
import types
from typing import Union


# Function that prints the name of a passed in function, and returns a new function
# encapsulating the behavior of the original function
def notify(fn, *args, **kwargs):
    def fncomposite(*args, **kwargs):
        # Normal notify functionality
        print("running %s" % fn.__name__)
        rt = fn(*args, **kwargs)
        return rt

    # Return the composite function
    return fncomposite


class Notifies(type):

    def __new__(cls, name, bases, attr):
        # Replace each function with
        # a print statement of the function name
        # followed by running the computation with the provided args and returning the computation result
        for name, value in attr.items():
            if type(value) is types.FunctionType or type(value) is types.MethodType:
                attr[name] = notify(value)

        return super().__new__(cls, name, bases, attr)


class Maths(metaclass=Notifies):
    def mult(self, a, b):
        return a * b


# >>> m.mult(3,4)
# running mult
# >>> 12


# the final class, can't be subclassed
class Final(type):
    def __new__(cls, name: str, bases: Union[list, tuple], attrs: dict):
        # check that Singleton has not been passed as a base class
        base_types = [type(base) for base in bases]
        for type_ in base_types:
            if type_ is Final:
                raise RuntimeError("Cannot Subclass Singleton")
        return super().__new__(cls, name, bases, attrs)


# auto logger
def _logs(fn, *a, **k):
    fname = fn.__name__

    def logs(*args, **kwargs):
        ret = fn(*args, **kwargs)
        msg = f"{fname} executed with args:{args}, and {kwargs}. Returned {repr(ret)}"
        print(msg)  # log here, using print as stub
        return ret

    return logs


def __static_logs(static):
    fn = static.__func__
    return _logs(fn)


class Logs(type):
    def __new__(cls, name, bases, attrs):
        for key, value in attrs.items():
            if type(value) is types.FunctionType or type(value) is types.MethodType:
                attrs[key] = _logs(value)
        return super().__new__(cls, name, bases, attrs)


if __name__ == '__main__':
    class foo(metaclass=Logs):
        @staticmethod
        def mult(a, b):
            return a * b
        def bar(self):
            return 'bar'


    a = foo()
    a.mult(2, 3)
    a.bar()
