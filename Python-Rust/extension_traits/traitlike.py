from abc import ABC, abstractmethod

# This is your "trait"
class Greet(ABC):
    @abstractmethod
    def greet(self) -> str:
        pass


# Extension "impl" for str via a wrapper
class StrGreet(Greet):
    def __init__(self, value: str):
        self.value = value

    def greet(self) -> str:
        return f"Hello, {self.value}!"


print(StrGreet("world").greet())  # Hello, world!

# OR #############

# def greet(self: str) -> str:
#     return f"Hello, {self}!"

# # Monkey patching str (not always recommended!)
# setattr(str, "greet", greet)

# print("world".greet())  # Hello, world!

# OR ##############
from functools import singledispatch

@singledispatch
def greet(value):
    raise NotImplementedError(f"No greet impl for {type(value)}")

@greet.register
def _(value: str):
    return f"Hello, {value}!"

print(greet("world"))  # Hello, world!
