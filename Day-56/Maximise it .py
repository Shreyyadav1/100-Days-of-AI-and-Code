from itertools import product

# Step 1: Read K (number of lists) and M (modulo)
K, M = map(int, input().split())

# Step 2: Store all lists
all_lists = []

for i in range(K):
    data = list(map(int, input().split()))
    
    # First value is length → ignore
    elements = data[1:]
    
    all_lists.append(elements)

# Step 3: Generate all combinations
all_combinations = product(*all_lists)

# Step 4: Initialize max value
max_value = 0

# Step 5: Check each combination
for comb in all_combinations:
    
    # Calculate sum of squares
    total = 0
    for x in comb:
        total += x * x
    
    # Apply modulo
    result = total % M
    
    # Update max
    if result > max_value:
        max_value = result

# Step 6: Print result
print(max_value)