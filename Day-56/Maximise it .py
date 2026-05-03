# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

# Read K and M
K, M = map(int, input().split())

# Store lists
all_lists = []

for i in range(K):
    data = list(map(int, input().split()))
    
    # Ignore first element (length)
    elements = data[1:]
    
    all_lists.append(elements)

# Initialize max value
max_value = 0

# Generate all combinations
for comb in product(*all_lists):
    
    total = 0
    
    # Calculate sum of squares
    for x in comb:
        total += x * x
    
    result = total % M
    
    if result > max_value:
        max_value = result

# Print result
print(max_value)
