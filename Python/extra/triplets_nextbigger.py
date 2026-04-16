from itertools import permutations

def next_bigger(n):
    ns = list(map(int,str(n)))
    for i in reversed(range(len(ns))):
        if i == 0: return -1
        if ns[i] > ns[i-1] :
            break        
    left, right = ns[:i], ns[i:]
    for k in reversed(range(len(right))):
        if right[k] > left[-1]:
           right[k], left[-1] = left[-1], right[k]
           break
    return int("".join(map(str,(left+sorted(right)))))
#     pers = [int("".join(p)) for p in permutations(list(str(n)))]
#     pers = [p for p in pers if p > n]
#     return min(pers) if pers else -1
    
from itertools import permutations

def next_bigger(n):
    lst = list(str(n))
    sor = sorted(lst, reverse=True)
    max = int("".join(sor))
    for i in range(n+1, max+1):
        if sorted(str(i)) == sorted(str(n)):
            return i
    return -1
# print(next_bigger(1111))
# print(next_bigger(24321))
# print(next_bigger(12))

class MyCycle(object):
    def __init__(self, lst):
        self.list = lst

    def __iter__(self):
        while True:
            items_left = False
            for x in self.list:
                if x is not None:
                    items_left = True
                    yield x
            if not items_left:
                return

    def remove(self, e):
        self.list[self.list.index(e)] = None

from itertools import cycle
def recoverSecret(triplets):
    answer = []
    
    stream = MyCycle(triplets)
    for s in stream:
        if not answer:
            answer = s
            stream.remove(s)
        else:
            putHere, dontRemove = None, False
            for el in s:
                try:
                    ind = answer.index(el)
                    putHere = ind
                except ValueError:
                    pass
                finally:
                    if putHere is not None and el not in answer:
                        answer = answer[0:putHere] + [el] + answer[putHere:]
                        putHere = None
                        s.remove(el)
                    elif putHere is not None and el in answer:
                        ind = answer.index(el)
                        if ind < putHere:
                            answer[ind], answer[putHere] = answer[putHere], answer[ind]
                    else:
                        answer += [el]
            if not s:
                stream.remove(s)
    return answer

from itertools import chain 

def recoverSecret(triplets):
    ans = list(set(chain.from_iterable(triplets)))
    for x, y, z in triplets*int(len(ans)/2):
        f1, f2, f3 = ans.index(x), ans.index(y), ans.index(z)
        if ( f1 > f2 ):
            ans[f1], ans[f2] = ans[f2], ans[f1]

        f1, f2, f3 = ans.index(x), ans.index(y), ans.index(z)
        if ( f2 > f3):
            ans[f2], ans[f3] = ans[f3], ans[f2]

        f1, f2, f3 = ans.index(x), ans.index(y), ans.index(z)
        if ( f1 > f3):
            ans[f1], ans[f3] = ans[f3], ans[f1]
    return "".join(ans)

# def recoverSecret(triplets): # best solution from online, sometimes wrong...
#   r = list(set([i for l in triplets for i in l]))
#   for l in triplets:
#     fix(r, l[1], l[2])
#     fix(r, l[0], l[1])
#   return ''.join(r)
  
# def fix(l, a, b):
#    """let l.index(a) < l.index(b)"""
#    if l.index(a) > l.index(b):
#        l.remove(a)
#        l.insert(l.index(b), a)

triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]
import random
random.shuffle(triplets)
print(recoverSecret(triplets))

def tower_builder(n_floors):
    # return [" "*(n_floors-i-1) + "*"*(i*2+1) + " "*(n_floors-i-1) for i in range(n_floors)]
    return "".join(("*" * (i*2+1)).center(n_floors*2-1)+"\n" for i in range(n_floors))

print(tower_builder(5))

from functools import reduce
def binary_array_to_number(arr):
    # return reduce(lambda s, x: [s[0]+x*2**s[1], s[1]-1] , arr, [0, len(arr)-1])[0]
    return int("".join(map(str, arr)), 2)
    # return reduce(lambda s, x: {'sum': s['sum']+x*2**s['pow'], 'pow': s['pow']-1} , arr, {'sum': 0, 'pow': len(arr)-1})['sum']

print(binary_array_to_number([1,0,1,0]))

from statistics import median
def is_triangle(a, b, c):
    print(median([a,b,c]))
    return min(a,b,c) > 0 and max(a,b,c) - min(a,b,c) < median([a,b,c])

print(is_triangle(7,2,2))

def other_angle(a, b):
    return 180 - a - b

from asyncio import sleep, run

class Foo:
    def __aiter__(self):
        self.i = 0
        return self
    async def __anext__(self):
        # await sleep(1)
        self.i += 1
        return self.i

async def using_async_for():
    async for bar in Foo():
        print(bar)
        if bar >= 10:
            break

# async def using_aiter_anext():
#     ai = aiter(Foo())
#     try:
#         while True:
#             bar = await anext(ai)
#             print(bar)
#             if bar >= 10:
#                 break
#     except StopAsyncIteration:
#         return

async def main():
    print("Using async for:")
    await using_async_for()

    # print("Using aiter/anext")
    # await using_aiter_anext()

if __name__ == '__main__':
    run(main())

from math import sqrt
x2len  = lambda x: sqrt(4*x**2 + 1)
sum = 0 
for i in range(0, 1000000):
    sum += x2len(i/1000000) * (1/1000000)
# this is correct ^^^
print("Sum", sum)

x2d  = lambda x: 2*x
sum = 0 
for i in range(0, 1000000):
    sum += x2d(i/1000000) * (1/1000000)
print("sumd", sum)

