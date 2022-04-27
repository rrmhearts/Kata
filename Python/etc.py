def persistence(n):
    pers = 0
    def recurse(n):
        total=1
        for e in f"{n}":
            total = total*int(e)
        return total
    while len(f"{n}") > 1:
        n = recurse(n)
        pers += 1
    return pers

# print(persistence(39))

import math
def bouncing_ball(h, bounce, window):
    total = -1
    if h < 0 or bounce < 0 or bounce > 1 or window > h:
        return -1
    #while h > window:
    #    h = h * bounce
    #    total += 2
    # h*bounce ^ n <= window
    # n * log(bounce) = log(window/h)

    
    return total + 2*math.ceil(math.log(window/h)/math.log(bounce))

# print(bouncing_ball(200, .7, 5))

def solution(args):
    ret = ""
    if not args:
        return ret
    temp = args[0]-1
    args.append(-999999999)
    range = []  
    for num in args:
        print(range, num, temp+1)
        if num == temp+1:
            range.append(num)
        else: # range ended
            if len(range) > 2:
                print("here", range)
                if ret:
                    ret = f"{ret},{range[0]}-{range[-1]}"
                else:
                    ret = f"{range[0]}-{range[-1]}"
            else:
                if ret:
                    ret = f"{ret},"
                for el in range:
                    ret += f"{el},"
                ret = ret[:-1]
            
            range = [num]
        temp = num
    return ret

# print(solution([-3,-2,-1,2,10,15,16,18,19,20]))
# print(solution([-96,-94,-93,-91,-89,-87,-85,-83,-81,-80,-79,-76,-75,-74,-72,-69,-66,-64,-63,-62,-60,-59,-56,-55,-53,-51,-49,-47,-46]))

norecurse = [0, 1]
def fibonacci(n: int) -> int:
    """Given a positive argument n, returns the nth term of the Fibonacci Sequence.
    """
    if len(norecurse) > n:
        return norecurse[n]
    print(n)
    norecurse[n] = norecurse[n-1] + norecurse[n-2]
    return norecurse[n]

# print(fibonacci(10))

import datetime
SECONDS_IN_DAY = (60*60*24)
SECONDS_IN_YEAR = (SECONDS_IN_DAY*365)
def format_duration(seconds):
    ret = ""
    if not seconds:
        return "now"
    years, seconds = divmod(seconds, SECONDS_IN_YEAR)
    if years:
        ret = f"{years} years" if years>1 else f"{years} year"
    # if seconds > 0: ret=f"{ret},"
    days, seconds = divmod(seconds, SECONDS_IN_DAY)
    if days:
        df = f"{days} days" if days>1 else f"{days} day"
        ret = f"{ret}, {df}" if ret and seconds else \
            f"{ret} and {df}" if ret and not seconds else \
            f"{df}"
    if seconds > 0:  
        timestr = str(datetime.timedelta(seconds=seconds)).split(':')
        units = ['hour', 'minute', 'second']
        for t, unit in zip(timestr, units):
            if int(t):
                if ret:
                    ret = f"{ret},"
                ret = f"{ret} {int(t)} {unit}s" if int(t)>1 \
                    else f"{ret} {int(t)} {unit}"
                ret = ret.lstrip()
        if len(ret.split(',')) > 1:
            start, _, last = ret.rpartition(",")
            return start + " and" + last
    return ret
# print(format_duration(9999999960))

def max_sequence(arr):
    if not arr:
        return 0
    max = (0, 0, 0)
    records = {}
    for i, item in enumerate(arr):
        sum = 0
        records[i] = {}
        for j, jtem in enumerate(arr[i:]):
            sum += jtem
            records[i][j] = sum
            
            if sum > max[2]:
                max = (i,j,sum)
    return max[2]
            
        
# print(max_sequence([3,3,6]))

import math

def remov_nb(n):
    ans = []
    sum = n * (n + 1) // 2
    for x in range(n):
        X = x+1
        aY = (sum-X)/(X+1)
        if 0 < aY <= n and aY == math.floor(aY):
            ans.append((x+1,aY))
    return ans

# print(remov_nb(26))

# from functools import lru_cache
# @lru_cache(maxsize=None)
def fibonacci2(n, cache={0:0,1:1}):
    if n in cache:
        return cache[n]
    cache[n] = fibonacci2(n - 1) + fibonacci2(n - 2)
    return cache[n]

# print(fibonacci2(1000))
arr = [1,2,3]
# print()

def is_interesting(number, awesome_phrases = []):

    for current in range(3):
        curr_number = number + current
        print(curr_number)
        arr = list(str(curr_number))
        intarr = [int(i) for i in arr]
        if len(set(arr)) == 1: # all same digit
            awesome_phrases.append(curr_number)
            print('all same', set(arr))
        if int(arr[0]) == sum(intarr):
            awesome_phrases.append(curr_number) # first digit non-zero
            print('allzero')
        if intarr == [i%10 for i in list(range(intarr[0],intarr[0]+len(intarr),1))]: # increment
            awesome_phrases.append(curr_number)
            print('increment')
        if intarr == list(range(intarr[0],intarr[0]-len(intarr),-1)): # decrement
            awesome_phrases.append(curr_number)
            print('decrem')
        if str(curr_number) == str(curr_number)[::-1]: #palindrome
            awesome_phrases.append(curr_number)
            print('palindrom')
    if number in [i for i in awesome_phrases] and number >= 100:
        return 2
    if number in [i-1 for i in awesome_phrases]:
        return 1
    if number in [i-2 for i in awesome_phrases]:
        return 1
    # print(awesome_phrases)
    return 0
# print(list(range(1,5,1)))
# print(is_interesting(98))
# print(is_interesting(99))

class RomanNumerals:
    conv = {
        'M': 1000, 'CM': 900, 
        'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
        'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 
        'V': 5, 'IV': 4, 'I': 1,
    }
    numconv = { 1000: 'M', 900: 'CM',
        500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
        50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
        5: 'V', 4: 'IV', 1: 'I'
    }
    def to_roman(val):
        roman = ""
        while (val > 0):
            for num in RomanNumerals.numconv:
                if num <= val:
                    val -= num
                    roman += RomanNumerals.numconv[num]
                    break
        return roman

    def from_roman(roman_num):
        i = 0
        number = 0
        while i < len(roman_num): # for each numeral
            for roman in RomanNumerals.conv:
                if roman in roman_num[i:] and roman_num[i:].index(roman) == 0:
                    number += RomanNumerals.conv[roman]
                    i += len(roman)
                    break
        return number


            # compound = slice(i, i+2, 1) # two characters
            # if roman_num[compound] in RomanNumerals.conv:
            #     number += RomanNumerals.conv[roman_num[compound]]
            #     i += 2
            # else: # else process a single character
            #     number += RomanNumerals.conv[roman_num[i]]
            #     i += 1
# print(RomanNumerals.from_roman('MMVIII'))
# print(RomanNumerals.from_roman('MDCLXVI'))
# print(RomanNumerals.from_roman('IV'))

# print(RomanNumerals.to_roman(1))    #, 'I', '1 should == "I"')
# print(RomanNumerals.to_roman(1990) )#, 'MCMXC', '1990 should == "MCMXC"')
# print(RomanNumerals.to_roman(2008) )#, 'MMVIII'
from math import ceil, sqrt
from time import perf_counter
# cache = {}
def decompose(n):
    def sumSquares(sq, m):
        if sq < 0:
            return None
        if sq == 0:
            return []
        # if sq in cache:
        #     return cache[(sq,m)]
        curr = min(m-1, ceil(sqrt(sq)) )
        while curr > 0:
            csq = sq-(curr)**2
            ret = sumSquares(csq, curr)
            if ret is not None:
                ret.append(curr)
                # cache[(sq,m)] = ret
                return ret
            curr -= 1
    return sumSquares(n**2, m=n)
        
# start = perf_counter()
# print(decompose(99999999))
# print(decompose(800))
# print(decompose(3000))
# print(decompose(1000))
# print(decompose(1000))
# print(decompose(2000))

# end = perf_counter()
# print("time:", (end-start))

from functools import reduce

def dirReduc(arr):
    opp = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST"
    }
    return reduce(lambda lst, y: lst[:-1] if lst and lst[-1]==opp[y] else lst+[y], arr, [])

a = ['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']

# print(dirReduc(a))

from itertools import cycle
class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.alphabet = alphabet
        self.key = key
        self.alphamod = lambda el, nx, dif: self.alphabet[(self.alphabet.index(el) + \
            dif*(self.alphabet.index(nx)+1) ) % len(self.alphabet)]
    def cipher(self, text, dif=1):
        key_cy = cycle(self.key)
        return "".join([self.alphamod(el, next(key_cy), dif) \
            if {el}.issubset(set(self.alphabet)) else next(key_cy) and el for el in text])
    def encode(self, text): return self.cipher(text)
    def decode(self, text): return self.cipher(text, -1)


abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
c = VigenereCipher(key, abc)

print(c.decode(c.encode('codewars')))
print(c.encode('CODEWARS'))
print(c.decode('laxxhsj'))
print(c.decode(c.encode("it's a shift cipher!")))

abc = u"アイウエオァィゥェォカキクケコサシスセソタチツッテトナニヌネノハヒフヘホマミムメモヤャユュヨョラリルレロワヲンー"
# abc = u"ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヽヾ"
key = u"カタカナ"
d = VigenereCipher(key, abc)

first = d.encode(u"カタカナ")
print(first)
print(d.decode(d.encode(u"カタカナ")))
print(d.decode(d.encode("サツサテ")))


def expanded_form(num):
    dot = str(num).index('.')
    return " + ".join(filter(lambda x: '.' not in x,\
        [v + '0'*(dot-i-1) if i < dot else f"{v}/{10**(i-dot)}" for i, v in enumerate(str(num))\
         if v.isdecimal() and v is not '0']) )

def expanded_form(num):
    dot = str(num).index('.')
    return " + ".join(filter(lambda x: '.' not in x,\
        [(v+'0'*(dot-i-1), f"{v}/{10**(i-dot)}")[i>dot]\
         for i, v in enumerate(str(num))\
         if v.isdecimal() and v is not '0']) )

# print(expanded_form(101.532))

from functools import reduce
def delete_nth(order,max_e):
    crit = {}
    def delop (s, x):
        crit[x] = crit.get(x, 0) + 1
        return s if crit[x] > max_e else s + [x]
        
    return reduce(delop, order, [])

# def delete_nth_slow(order,max_e):
#     ans = []
#     for o in order:
#         if ans.count(o) < max_e: ans.append(o)
#     return ans

# from time import perf_counter
# import random
# start = perf_counter()
# i = 1000
# while i > 0:
#     delete_nth(\
#         [random.randint(1, 40) for i in range(random.randint(50, 1000))], random.randint(1,5))
#     i -= 1
# print("Time mine", perf_counter()-start)

# start = perf_counter()
# i = 1000
# while i > 0:
#     delete_nth_slow(\
#         [random.randint(1, 40) for i in range(random.randint(50, 1000))], random.randint(1,5))
#     i -= 1
# print("Time slow", perf_counter()-start)

def retHello():
    some = [104, 101, 111]
    blah = "d" + ().__class__.__eq__.__class__.__name__[:2] + str(str.__class__)[2]
    some.extend(sorted(blah))
    some.insert(2, some[4]*2)
    some[4], some[-1] = some[-1], some[4]
    some[5], some[-2] = some[-2], some[5]
    return "".join( chr(a) if type(a)==int else a for a in some[0:-3] + [True.__class__.__name__[1]] + some[-3:] ).replace("lo", "lo ")+"!"
    # 104, 101, 108, 108, 111
    # 'o' True.__class__.__name__[1]
    # 'wr' ().__class__.__eq__.__class__.__name__[:2]
from subprocess import check_output

greet = lambda: check_output(["python", "-c", "import __hello__"]).decode('ascii').lower()[:-1]

    # 108, 100, 33
print(greet())

def string_to_array(s):
    ans = []
    continued = False
    for i, el in enumerate(s):
        if el == " ":
            continued = True
        else:
            try:
                word = s[i:(i+s[i:].index(" "))]
            except ValueError:
                word = s[i:]
            if not ans or continued:
                ans.append(word.strip())
            continued = False
    if not ans: return ['']
    return ans
# print(string_to_array("IYizDVBSD4mSWv97cyg1 qxV5laYKB6qgz6 XpTK3oAXRQqxCY rX7wPfijbCN9jw i nBcffOx2nsCxx2 JerE33p4 UN"))

# @total_ordering
class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    @classmethod
    def card(self, cardName):
        return self(cardName[:-1], cardName[-1])

    def __str__(self):
        return '%s of %s' % (self.rank,
                             self.suit)

    def __repr__(self): return str(self)

    def __lt__(self, other):
        t1 = self.suit, self.numerize(self.rank)
        t2 = other.suit, self.numerize(other.rank)
        return t1 < t2

    def __gt__(self, other):
        t1 = self.suit, self.numerize(self.rank)
        t2 = other.suit, self.numerize(other.rank)
        return t1 > t2

    def __eq__(self, other):
        t1 = self.suit, self.numerize(self.rank)
        t2 = other.suit, self.numerize(other.rank)
        return t1 == t2

    def numerize(rank):
        if rank[0] == "A": return 14
        if rank[0] == "K": return 13
        if rank[0] == "Q": return 12
        if rank[0] == "J": return 11
        return int(rank)

def stf(cards):
    ordered = sorted(cards, reverse=True)
    for i, e in enumerate(ordered):
        print(i,e)
    return 5
dict = {
    "straight-flush": stf
}
def hand(hole_cards, community_cards):
    stf(hole_cards+community_cards)
    return "nothing", ["2", "3", "4", "7", "8"]


print(hand(["8♠", "6♠"], ["7♠", "5♠", "9♠", "J♠", "10♠"]))
            # ("straight-flush", ["J", "10", "9", "8", "7"]),
print(hand(["K♠", "A♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"]))
            # ("nothing", ["A", "K", "Q", "J", "9"]),
print(hand(["K♠", "Q♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"]))
            # ("pair", ["Q", "K", "J", "9"]),


puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solution = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]]

import itertools
allset = {1,2,3,4,5,6,7,8,9}
dict = {}
def updateDict(keys, goset, puzzle):
    for each in keys:
        try:
            dict[each] = dict[each].intersection(goset)
        except KeyError:
            dict[each] = goset
        if len(dict[each]) == 1 and None not in each:
            puzzle[each[0]][each[1]] = dict[each].pop()

def threeByThree(puzzle, fi, fj):
    for i in range(3*(fi//3),len(puzzle),3):
        for j in range(3*(fj//3),len(puzzle[i]),3):
            items = allset - {
                puzzle[i][j],   puzzle[i][j+1],   puzzle[i][j+2],
                puzzle[i+1][j], puzzle[i+1][j+1], puzzle[i+1][j+2],
                puzzle[i+2][j], puzzle[i+2][j+1], puzzle[i][j+2]
            }
            updateDict([(x,y) for x,y in \
                        [(i,j),(i,j+1),(i,j+2),
                         (i+1,j),(i+1,j+1),(i+1,j+2),
                         (i+2,j),(i+2,j+1),(i+2,j+2)]
                         if puzzle[x][y] == 0 
                    ], items, puzzle)
    return puzzle

def colRow(puzzle, fi, fj):
    global allset
    cols = []
    for i in range(fi, len(puzzle)): # each row
        updateDict([(i,j) for j in range(0,9) if puzzle[i][j] == 0], \
            allset - set(puzzle[i]), puzzle )
        for j, el in enumerate(puzzle[i]):
            if len(cols) < j+1:
                cols.append([])
            cols[j].append(el)
    for j in range(fj, len(cols)):
        updateDict([(i,j) for i in range(0,9) if puzzle[i][j] == 0], \
            allset - set(cols[j]), puzzle)
    return puzzle
def next0(puzzle, i):
    for i in range(len(puzzle)):
        try:
            j = puzzle[i].index(0)
            return i,j
        except ValueError:
            pass
    return 0, 0
def sudoku(puzzle):
    global allset
    i, j = 0, 0
    count = list(itertools.chain(*puzzle)).count(0)
    while count > 0:
        # for _ in range(count//2):
        puzzle = colRow(puzzle, i,j)
        puzzle = threeByThree(puzzle, i,j)
        i,j = next0(puzzle, i)
        # temp = {c for c in allset\
        #     if list(itertools.chain(*puzzle)).count(c)==9}
        
        # allset = allset - temp
        # print(temp, allset)
        count = list(itertools.chain(*puzzle)).count(0)

    return puzzle

print(sudoku(puzzle))