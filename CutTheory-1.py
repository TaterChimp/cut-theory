from fractions import Fraction

class Cut:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.pieces = m * (n + 1)
        self.size = Fraction(1, 1) / (n + 1)

    def __str__(self):
        return f"({self.pieces}, {self.size})"

# user input
m = Fraction(input("Enter m (like 1/2): "))
n = Fraction(input("Enter n (like 1/2): "))

c = Cut(m, n)

print(c)