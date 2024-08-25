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

    noon_sat = (noon[0] == center[3] and noon[5] == ten[2] and noon[1] == two[4])
    two_sat = two[0] == four[3] and two[5] == center[4] #and two[2] == noon[5]
    four_sat = four[5] == six[2] and four[4] == center[1] #and four[3] == two[0]
    six_sat = six[4] == eight[1] and six[3] == center[0] #and six[4] == four[1]
    eight_sat = eight[3] == ten[0] and eight[2] == center[5] #and eight[5] == six[2]
    ten_sat = ten[0] == eight[3] and ten[1] == center[4] #and ten[4] == noon[1]

    if noon_sat and two_sat and four_sat and six_sat and eight_sat and ten_sat:
        print(center)
        print(noon_2468_10)

    return noon_sat and two_sat and four_sat and six_sat and eight_sat and ten_sat

def generate_rotations(wheels):
    new_wheels = []
    for i in range(6):
        for j in range(6):
            for k in range(6):
                for l in range(6):
                    for m in range(6):
                        for n in range(6):
                            for o in range(6):
                                yield [
                                    rotate(wheels[0], i),
                                    rotate(wheels[1], j),
                                    rotate(wheels[2], k),
                                    rotate(wheels[3], l),
                                    rotate(wheels[4], m),
                                    rotate(wheels[5], n),
                                    rotate(wheels[6], o)
                                ]

if __name__ == '__main__':
    wheels_original = [
        [1,3,5,4,2,6],
        [1,2,3,4,5,6],
        [1,3,5,2,4,6],
        [1,2,5,6,3,4],
        [1,6,5,4,3,2],
        [1,4,2,3,5,6],
        [1,5,3,2,6,4]
    ]
    
    for wheels in generate_rotations(wheels_original):

        # while (hash(str(wheels)) in hashes):
        #     rot_el = random.randint(0, len(wheels)-1)
        #     wheels[rot_el] = rotate(wheels[rot_el], 1)
        # hashes.append( hash(str(wheels)) )
        # wheels[wheel] = rotate(wheels[wheel], 1)

        for i, center in enumerate(wheels):
            outside_els = list(skip_i(wheels, i))

            for specific_order in it.permutations(outside_els, len(outside_els)):
                if compare(center, outside_els):
                    print("center:", center)
                    print("noon_around:", outside_els)
                    unfinished = False
                    exit()
        # print(center, f"lenght outside: {len(outside_els)}")
        # print("      ", outside_els)
    print("finsihed?")
# pick one to be the center, 

# for center in wheels:
# for remainder wheels get every ordering
