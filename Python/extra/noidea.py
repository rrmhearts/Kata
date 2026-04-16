def fib(n, keeper = {}):
    org, even = n, n%2==0
    mk = 0
    if n < 0:
        return -fib(-n, keeper) if even else fib(-n, keeper)
    a, b = 0, 1
    if org in keeper:
        return keeper[org][0]
    else:
        mk = max(keeper.keys())
        a, b = keeper[mk]
    while n-mk > 0:
        a, b = b, a+b
        n -= 1
    keeper[org] = (a, b)
    return a

# from numpy import matrix

# def fib(n):
#     return (matrix(
#         '0 1; 1 1' if n >= 0 else '-1 1; 1 0', object
#         ) ** abs(n))[0, 1]
        
# print(fib(-1000))

#product = 4*10**(len(x)-1) + ((x - n)/10)


def calc_special( lastDigit,base ):

    def from_base(digits):
        try:
            return int(digits, base)
        except ValueError:
            return 0
    def to_base(digits):
        if base == 8:
            return oct(digits)[2:]
        elif base == 16:
            return hex(digits)[2:]
        return digits
    
    strld = str(lastDigit)
    fbld = from_base(strld)
    order = 2
    while True:
        for i in range(from_base(str(lastDigit*10**order)), from_base(str((lastDigit + 1)*10**order))):
            value = str(to_base( i // fbld))
            if value[-1] == strld and value[:-1] == str(to_base(i))[1:]:
                return str(value)
        order += 1


def calc_special( lastDigit, base ):
    def from_base(digits):
        try:
            return int(digits, base)
        except ValueError:
            return 0
    def to_base(digits):
        if base == 8:
            return oct(digits)[2:]
        elif base == 16:
            return hex(digits)[2:]
        return digits
    newone = f"{to_base(lastDigit)}"
    counter = -1
    while True:
        value = str(to_base(lastDigit*from_base(newone)))
        if value[0] == str(to_base(lastDigit)) == newone[-1] and value[1:] == newone[:-1]:
            return newone
        elif value == 0:
            return ""
        newone = value[counter] + newone 
        counter -= 1
print(calc_special(4, 16))
print(calc_special(9, 16))

print(calc_special(4,10))
print(calc_special(2,8))
print(calc_special(6,10))
#102564
#1016
print(calc_special(7,10))
print(calc_special(5,10))
print(calc_special(0xF,16))