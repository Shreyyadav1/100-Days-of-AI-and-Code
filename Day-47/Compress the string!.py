from itertools import groupby

# Step 1: Take input string
s = input()

# Step 2: Apply groupby
groups = groupby(s)

# Step 3: Store results
result = []

for key, group in groups:
    
    # Step 4: Count occurrences
    count = len(list(group))
    
    # Step 5: Convert key to int
    digit = int(key)
    
    # Step 6: Store tuple
    result.append((count, digit))

# Step 7: Print output
for item in result:
    print(item, end=" ")