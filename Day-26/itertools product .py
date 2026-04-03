from itertools import product

# Read first list and convert each value to int
A = list(map(int, input().split()))

# Read second list and convert each value to int
B = list(map(int, input().split()))

# Generate cartesian product
result = product(A, B)

# Print tuples in the required format
print(*result)