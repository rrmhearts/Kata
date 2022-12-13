
def chunker(iterable, chunksize):
    return zip(*[iter(iterable)] * chunksize)

def intersection(*args):
    intset = set()
    for pk in args:
        if intset == set():
            intset.union(pk)
        else:
            intset.intersection(pk)
    return intset.pop()

with open('backpacks.txt', 'r') as f:
    contents = f.read().split('\n');

    dups = []
    for pack in contents:
        half = int(len(pack) /2)
        p1 = set(pack[0:half])
        p2 = set(pack[half:])
        dup = ord(p1.intersection(p2).pop())
        dups.append(dup - 96 if dup > 96 else dup - 64 + 26)


    print("Part 1: ", sum(dups))

    ids = []
    for g1, g2, g3 in chunker(contents,3):
        id = ord(set(g1).intersection(set(g2)).intersection(set(g3)).pop())
        ids.append( id - 96 if id > 96 else id - 64 + 26)

    print("Part 2: ", sum(ids))