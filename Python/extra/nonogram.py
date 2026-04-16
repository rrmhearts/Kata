# X = ['A', 'B', 'C']
# D = {
#     'A': [1, 2, 3],
#     'B': [1, 2, 3],
#     'C': [1, 2, 3]
# }
# C1 = {}
# C2 = {
#     ('A', 'B'): [lambda a, b: a > b],
#     ('B', 'A'): [lambda b, a: b < a],
#     ('B', 'C'): [lambda b, c: b == c],
#     ('C', 'B'): [lambda c, b: c == b],
# }


from itertools import product
from functools import partial
class Nonogram:
# >>> from functools import partial
# >>> def f(a, b, c):
# ...   print a, b, c
# ...
# >>> bound_f = partial(f, 1)
# >>> bound_f(2, 3)
# 1 2 3
    def __init__(self, clues):
        self.CC, self.RC = clues
        self.nc, self.nr = len(self.CC), len(self.RC)
        self.X = [("RC",_) for _ in range(self.nr)] # [("CC",_) for _ in range(self.nc)]
        self.D = { key: list(product(["0","1"], repeat=self.nc) ) for key in self.X}
        self.C1 = {
            var: [self.row_check, self.col_check, self.fitsothers_check ]#partial(self.row_check, var)(a) ] \
                  for var in self.X #getattr(self, var[0])[var[1]]
        }
        self.C2 = {
            # (var, oth): [lambda a, b: self.D[a][b[1]] == self.D[b][a[1]]] \
            #     for var in self.X for oth in self.X #if oth[0]!=var[0]
            (x, y): [lambda v1, v2, x1, y2: v1[y2[1]] == v2[x1[1]] ] \
                for x in self.X for y in self.X if x[0] != y[0]
        }
    def fitsothers_check(self, cons, arr, x=None):
        if x is None:
            return True
        y0 = 'RC' if x[0] == 'CC' else 'CC'
        location = x[1]
        for v in self.X:
            if v[0] == y0 and not any(vx[location] == arr[v[1]] for vx in self.D[v]): # row or col
                return False
        return True

    def col_check(self, _, arr, x=None):
        rows = []
        # print('ar', arr)
        for row in self.X:
            if row != x:
                print(x, self.D[row])
                rows.append(self.D[row])
            else: rows.append(arr)
        print("rows", rows)
        cols = [[] for _ in rows]
        for i,vx in enumerate(rows):
            for j,y in enumerate(vx):
                cols[j].append(y)
        # print(rows, "\n", cols)
        # for i, c in enumerate(self.CC):
        #     print(c, cols[i], self.row_check(c, cols[i]))
        return all(self.row_check(c, cols[i]) for i,c in enumerate(self.CC))

    def row_check(self, cons, arr, x=None):
        index = 0
        for c in cons:
            try:
                nex = max(index, arr.index('1'))
            except ValueError:
                return False
            if not "1"*c in "".join(arr[nex:]) or arr[nex] != '1':
                return False
            index = nex + c
            if index < len(arr) and arr[index] == '1':
                return False
            index += 1
        if '1' in arr[index:]:
            return False
        # print("checker", cons, arr, index)
        return True
    
    def solve(self):
        RightD = self.ac3(self.X, self.C1, self.C2)

        return tuple(tuple(int(i) for i in v[0]) for k, v in RightD.items() if k[0] == 'RC')
        

    def ac3 (self, X, R1, R2):
        for x in X: #for each row and column
            # print(x, getattr(self, x[0])[x[1]])
            xConds = getattr(self, x[0])[x[1]] # CONSTRAINT for one ROW , cols out of variables now
            self.D[x] = [vx for vx in self.D[x] if all(map(lambda f: f(xConds,vx,x), R1.get(x,[]))) ]
            # newDomain = []
            # for i, vx in enumerate(self.D[x]):
            #     # if not self.row_check(xConds, vx):
            #     #     self.D[x].remove(vx)
            #     if self.row_check(xConds, vx):
            #         newDomain += [vx]
            # self.D[x] = newDomain
            # print("Survived", self.D[x])
        worklist = [rel for rel in R2.keys()] # all arcs
        while worklist:
            x, y = worklist.pop()
            if self.arcreduce (x, y, self.D, R2):
                if not self.D[x]:
                    return False
                else:
                    worklist = worklist + [rel for rel in R2.keys() if rel[1] == x]
        return self.D

    def arcreduce (self, x, y, D, R2):
        change = False
        vy_satisfies_R2 = []
        for vx in D[x]:
            for vy in D[y]:
                # print("arc", x, y, vx, vy)
                if all(map(lambda f: f(vx,vy,x,y), R2.get((x,y),[]))): # get the rules for (x,y)
                    vy_satisfies_R2.append(vy)
            # vy_satisfies_R2 = list(filter(None, [vy if all(map(lambda f: f(vx,vy), R2.get((x,y),[]))) else None for vy in D[y]]) )
            if not vy_satisfies_R2:
                D[x].remove(vx)
                change = True
            # except KeyError:
            #     print(x, vx, D[x])
        return change

clues = (((1, 1), (4,), (1, 1, 1), (3,), (1,)),
          ((1,), (2,), (3,), (2, 1), (4,)))

ans = ((0, 0, 1, 0, 0),
       (1, 1, 0, 0, 0),
       (0, 1, 1, 1, 0),
       (1, 1, 0, 1, 0),
       (0, 1, 1, 1, 1))

non = Nonogram(clues)
print("solved", non.solve())