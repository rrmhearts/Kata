from typing import TypeVar, Generic, List, Sequence
# from collections.abc import Sequence

T = TypeVar('T')

# Python 3.12 support this new syntax for generic types
## def get_first[T](collection: Sequence[T]) -> T:
def get_first(collection: Sequence[T]) -> T:
    # Any works but no feedback from type checker
    return collection[0]

people: List[str] = ['Alice', 'Bob', 'Charlie']
first_person: str = get_first(people)
print(first_person)

K, V = TypeVar('K'), TypeVar('V')
def get_id(db: dict[K, V], user: K) -> V: # type: ignore
    return db[user]

users: dict[str, int] = {'bob': 0, 'james': 1, 'alice': 2}
value: int = get_id(users, 'bob')
print(value)

changeTypes: dict[int, str] = {0: 'zero', 1: 'one', 2: 'two'}
value2: str = get_id(changeTypes, 1)
print(value2)

# Python 3.12 supports the new syntax for generic types
## class CustomList[T]:
class CustomList(Generic[T]):
    def __init__(self, items: List[T]) -> None:
        self.items = items

    def get(self, index: int) -> T:
        return self.items[index]
    
    def append(self, item: T) -> None:
        self.items.append(item)

    def get_items(self) -> List[T]:
        return self.items
    
    def remove(self, item: T) -> None:
        if item in self.items:
            self.items.remove(item)

cl: CustomList[int] = CustomList([1, 2, 3])
# c2: CustomList[int] = CustomList(['a', 'b'])

cl.append(4)
print(cl.get(0))  # Output: 1
print(cl.get_items())  # Output: [1, 2, 3, 4]

# Type annotations are not enforced at runtime, 
# but they help with static type checking
# cl.append('a')
# need to use mypy to check types
## python -m mypy .\generics.py 
## generics.py:56: error: Argument 1 to "append" of "CustomList" has incompatible type "str"; expected "int"  [arg-type]
## Found 1 error in 1 file (checked 1 source file)