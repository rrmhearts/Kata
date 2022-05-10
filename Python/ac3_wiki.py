# Problem Representation

#     For illustration, here is an example of a very simple constraint 
# problem: X (a variable) has the possible values {0, 1, 2, 3, 4, 5}
# -- the set of these values are the domain of X, or D(X). The 
# variable Y has the domain D(Y) = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}. 
# Together with the constraints C1 = "X must be even" and 
# C2 = "X + Y must equal 4" we have a CSP which AC-3 can solve. 
# Notice that the actual constraint graph representing this problem 
# must contain two edges between X and Y since C2 is undirected but 
# the graph representation being used by AC-3 is directed.

#   It does so by first removing the non-even values out of the domain of 
# X as required by C1, leaving D(X) = { 0, 2, 4 }. It then examines the arcs 
# between X and Y implied by C2. Only the pairs (X=0, Y=4), (X=2, Y=2), and 
# (X=4, Y=0) match the constraint C2. AC-3 then terminates, with D(X) = {0, 2, 4} 
# and D(Y) = {0, 2, 4}.

# X = ['x', 'y'] # variables to solve for
# domain = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# D = { key: domain for key in X}
# C1 = {
#         'x': [ lambda x: x % 2 == 0, lambda y: y * y > 10 ],
# }
# C2 = {
#     ('x','y'): [ lambda x, y: x+y == 12],
#     ('y','x'): [ lambda x, y: x+y == 12],
# }
X = ['A', 'B', 'C']
D = {
    'A': [1, 2, 3],
    'B': [1, 2, 3],
    'C': [1, 2, 3]
}
C1 = {}
C2 = {
    ('A', 'B'): [lambda a, b: a > b],
    ('B', 'A'): [lambda b, a: b < a],
    ('B', 'C'): [lambda b, c: b == c],
    ('C', 'B'): [lambda c, b: c == b],
}

# Input:
#    A set of variables X
#    A set of domains D(x) for each variable x in X. D(x) contains vx0, vx1... vxn, 
#           the possible values of x
#    A set of unary constraints R1(x) on variable x that must be satisfied
#    A set of binary constraints R2(x, y) on variables x and y that must be satisfied
   
#  Output:
#    Arc consistent domains for each variable.

def ac3 (X, D, R1, R2):
    for x in X:
        D[x] = [vx for vx in D[x] if all(map(lambda f: f(vx), R1.get(x,[]))) ]
    worklist = [rel for rel in R2.keys()] # all arcs
    while worklist:
        x, y = worklist.pop()
        if arcreduce (x, y, D, R2):
            if not D[x]:
                return False
            else:
                worklist = worklist + [rel for rel in R2.keys() if rel[1] == x]
    return D

def arcreduce (x, y, D, R2):
     change = False
     for vx in D[x]:
         vy_satisfies_R2 = list(filter(None, [vy if all(map(lambda f: f(vx,vy), R2.get((x,y),[]))) else None for vy in D[y]]) )
         if not vy_satisfies_R2:
             D[x].remove(vx)
             change = True
     return change

print(ac3(X, D, C1, C2) )