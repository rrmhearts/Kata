from z3 import Int, Solver, sat, simplify

x = Int('x')
y = Int('y')
z = Int('z')
s = Solver()

# s.add( (x % 4) + 3 * (y /2) > x-y)
s.add( 3*x + 2*y - z == 1)
s.add( 2*x -2*y + 4*z == -2)
s.add( x + y + z == 222)
if s.check() == sat:
    print(s.model())
else:
    print("unsat")

print(simplify(x+1+y+x+1))
print(simplify(5*(2+x)+3*(5*x+4)-x**2))