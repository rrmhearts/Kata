
class Tester:
    def __init__(self, value):
        self.value = value # should be list(value) to avoid pass by reference
        self.rightway = list(value)

    def display(self):
        print(f"Current value: {self.value}")
        print(f"rightway: {self.rightway}")

alist = list(range(10))

tt = Tester(alist)
tt.display()
# This affects Tester's list!
alist.pop(0)
tt.display()

# Current value: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Current value: [1, 2, 3, 4, 5, 6, 7, 8, 9]