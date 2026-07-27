class Car(Vehicle):              # inheritance
    def __init__(self, x):
        super().__init__(x)      # call parent ctor
        self.__hidden = x        # name-mangled, not truly private

    @property                    # getter
    def hidden(self): return self.__hidden
    @hidden.setter                # setter — same name as getter
    def hidden(self, v): self.__hidden = v

# ── CHECK MRO before assuming override order ──
class C(A, B): pass
print(C.__mro__)                 # leftmost parent wins conflicts, by default

# ── isinstance ──
isinstance(obj, SomeClass)       # like Java's instanceof

# ── ABSTRACT CLASS ──────────────────────────
import abc
class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self): pass          # must be implemented by subclass

# ── DUNDER METHODS (operator overload) ──────
__init__      # constructor
__str__       # print(obj) / str(obj)
__eq__        # ==      (define __ne__ too if you need it — not automatic)
__lt__        # <       (define __le__ too if you need it — not automatic)
__add__       # +
__getitem__   # obj[k]
__contains__  # x in obj
__bool__      # bool(obj)

# ── CLOSURE ──────────────────────────────────
def make_counter():
    n = 0
    def inc():
        nonlocal n     # REQUIRED to *mutate* outer var — reading alone doesn't need it
        n += 1
        return n
    return inc

# ── DECORATOR ────────────────────────────────
def my_decorator(func):
    def wrapper(*args, **kwargs):   # ALWAYS *args, **kwargs unless func truly takes none
        # do something before
        result = func(*args, **kwargs)
        # do something after
        return result
    return wrapper

@my_decorator
def some_func(a, b): ...