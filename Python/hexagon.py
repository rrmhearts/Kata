# Birthday 08/17/2024 received a game that needs to be solved...
import itertools as it
import random
import pickle
def rotate(l, n):
    return l[n:] + l[:n]

def skip_i(iterable, i):
    itr = iter(iterable)
    return it.chain(it.islice(itr, 0, i), it.islice(itr, 1, None))


def compare(center, noon_2468_10):

    noon  = noon_2468_10[0]
    two   = noon_2468_10[1]
    four  = noon_2468_10[2]
    six   = noon_2468_10[3]
    eight = noon_2468_10[4]
    ten   = noon_2468_10[5]

    noon_sat = (noon[0] == center[3] and noon[1] == ten[4] and noon[5] == two[2])
    two_sat = two[0] == four[3] and two[1] == center[4] #and two[2] == noon[5]
    four_sat = four[1] == six[4] and four[2] == center[5] #and four[3] == two[0]
    six_sat = six[2] == eight[5] and six[3] == center[0] #and six[4] == four[1]
    eight_sat = eight[3] == ten[0] and eight[4] == center[1] #and eight[5] == six[2]
    ten_sat = ten[0] == eight[3] and ten[5] == center[2] #and ten[4] == noon[1]

    return noon_sat and two_sat and four_sat and six_sat and eight_sat and ten_sat

def generate_rotations(wheels):
    for i in range(len(wheels)):
        for j in range(6):
            yield i, j

if __name__ == '__main__':
    wheels = [
        [1,3,5,4,2,6],
        [1,2,3,4,5,6],
        [1,3,5,2,4,6],
        [1,2,5,6,3,4],
        [1,6,5,4,3,2],
        [1,4,2,3,5,6],
        [1,5,3,2,6,4]
    ]
    hashes = []
    with open('hashes.pickle',"rb") as hs:
        hashes = pickle.load(hs)

    
    unfinished = True
    while (unfinished):

        while (hash(str(wheels)) in hashes):
            rot_el = random.randint(0, len(wheels)-1)
            wheels[rot_el] = rotate(wheels[rot_el], 1)
        hashes.append( hash(str(wheels)) )

        for i, center in enumerate(wheels):
            outside_els = list(skip_i(wheels, i))

            for specific_order in it.permutations(outside_els, len(outside_els)):
                if compare(center, outside_els):
                    print("center:", center)
                    print("noon_around:", outside_els)
                    unfinished = False
                    exit()
        with open('hashes.pickle', 'wb') as hs:
            pickle.dump(hashes, hs)
        # print(center, f"lenght outside: {len(outside_els)}")
        # print("      ", outside_els)

# pick one to be the center, 

# for center in wheels:
# for remainder wheels get every ordering
