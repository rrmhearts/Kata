
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