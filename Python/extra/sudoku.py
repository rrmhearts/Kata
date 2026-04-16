
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
def updateDict(keys, goset, puzzle, dict =dict(), twos=dict()):
    for each in keys:
        valueBeGone = set()
        try:
            dict[each] = dict[each].intersection(goset)
        except KeyError:
            dict[each] = goset
        if len(dict[each]) == 1 and None not in each:
            puzzle[each[0]][each[1]] = dict[each].pop()
        if len(dict[each]) == 2 and None not in each:
            twos[each] = dict[each]
            for k, v in twos.items():
                if dict[each] == v and each != k:
                    valueBeGone = valueBeGone.union(v)
                    # if each[0]==k[0]:
                    #     for k,v in dict.items():
                            
                    # if each[1] ==k[1]:


def threeByThree(puzzle, fi, fj):
    i = 3*(fi//3)
    j = 3*(fj//3)
    items = {1,2,3,4,5,6,7,8,9} - {
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
    updateDict([(fi,j) for j in range(0,9) if puzzle[fi][j] == 0], \
        {1,2,3,4,5,6,7,8,9} - set(puzzle[fi]), puzzle )
    updateDict([(i,fj) for i in range(0,9) if puzzle[i][fj] == 0], \
        {1,2,3,4,5,6,7,8,9} - set([puzzle[i][fj] for i in range(0,9)]), puzzle)
    return puzzle

def nextFind(puzzle):
    i,j = 0,0
    while True:
        try:
            offj = puzzle[i][j:].index(0)
            j = j + offj
            yield i, j
            j += 1
        except ValueError:
            j = 0
            i = (i + 1) % len(puzzle)
            yield i, j
        i = (i + j//9) % len(puzzle)
        j = j % len(puzzle[i])

def sudoku(puzzle):
    global allset
    i, j = 0, 0
    count = list(itertools.chain(*puzzle)).count(0)
    gen = nextFind(puzzle)
    while count > 0:
        i,j = next(gen)
        puzzle = colRow(puzzle, i,j)
        puzzle = threeByThree(puzzle, i,j)
        count -= 1
        if count <= 3:
            count = list(itertools.chain(*puzzle)).count(0)
    return puzzle

print(sudoku(puzzle))