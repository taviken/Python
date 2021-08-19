import fibonacci
import nested


def a(b):
    c = fibonacci.fib(b)
    nested.nest(c)
    exec('import hello_world')
    return False


def deep(a, b, c, d, e, f):
    if a:
        if b:
            if c:
                if d:
                    if e:
                        if f:
                            print('how d you make it here?')
