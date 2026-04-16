# from memory_profiler import profile
from guppy import hpy
hp = hpy()
# print(hp.heap())
# @profile
def main():
    a = []
    b = []
    c = []
    for i in range(100000):
        a.append(5)
    for i in range(100000):
        b.append(300)
    for i in range(100000):
        c.append('123456789012345678901234567890')
    del a
    del b
    del c

if __name__ == '__main__':
    hp.setrelheap()

    main()
    h = hp.heap()
    print(h)
    print ('Done!')