# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['say_hello', 'HelloSayer', 'proportion', 'FtoC', 'CtoF']

# Cell
def say_hello(to):
    "Say hello to somebody"
    return f'Hello {to}!2'

# Cell
class HelloSayer:
    "Say hello to `to` using `say_hello`"
    def __init__(self, to): self.to = to

    def say(self):
        "Do the saying"
        return say_hello(self.to)

# Cell

def proportion(a, b):
    """
    We can use triple " to describe what our function does.

    Here for example: we're creating a function to calculate
    the proportion of a of a + b
    """
    return a / (a + b)


# Cell

def FtoC(x):
    """
    Escribe el valor de la temperatura en °C

    """
    return ((9/5)*x)+32


# Cell

def CtoF(x):
    """
    Escribe el valor de la temperatura en °F

    """
    return ((x-32)/(9/5))
