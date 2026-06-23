def cut(m, n):
    pieces = m * (n + 1)
    size = 1 / (n + 1)
    return pieces, size

m = int(input("Enter a number: "))
n = int(input("Enter the number of times to cut that number: "))

pieces, size = cut(m, n)

print("Pieces:", pieces)
print("Size of each:", size)