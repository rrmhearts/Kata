## Weird and Obtuse Python Code Examples

a: list[str] = ['a', 'b', 'c', 'd', 'e' 'f']
# if you forget a comma, it will be concatenated
print(len(a))
'e' 'f' # becomes 'ef'

# Try/except for control and flow
a, b = 1, 0
try:
    result = a / b
except ZeroDivisionError as e:
    # Wrong way to handle it
    result = 0
print(result)

# Multiple assignments with same name
text, text = 'eggs', 'ham'
print(text, text)

data: tuple[str, str] = 'A1', 'B2'
print(dict(data)) # {'A': '1', 'B': '2' }

# Multiple comparison riddle
comparison: bool = [] == [] == []
print(comparison) # True WTF
# evals like [] == [] and [] == []

# Pistol operator
*_, = 'Bob'
print(_) # ['B', 'o', 'b']

# 
result: int = 1 ++----++----++-+-+ 1
# Becomes 1 +++++ 1 ==> 1 + 1
print(result) # 2

_ = 1
__ = 2
___ = 3
result: int = _--__---___--_+-_+__
print(result) # 2

# IIFE - Immediately Invoked Function Expression
from datetime import datetime
@lambda _: _()
def start() -> str:
    now: datetime = datetime.now()
    return f'{now: %c}'
# same as start_time = f'{datetime.now(): %c}'
print(start)

# Cyrillic e character would break this.
entry: int = 10
print(entry)

print('Cyrillic:', ord('e'))

# Flatten and filter even number and square them if row+col is odd
# With LIST COMPREHENSIONS
matrix: list[list[int]] = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
result: list[int] = [
    num
    for sublist in [
        [
            row[col] **2 if (row_idx + col) % 2 == 1 and row[col] % 2 == 0 else None
            for col in range(len(row))
        ]
        for row_idx, row in enumerate(matrix)
    ]
    for num in sublist
    if num is not None
] # Wild if on one line
print(result)