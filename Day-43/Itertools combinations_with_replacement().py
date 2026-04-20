from itertools import combinations_with_replacement

# Step 1: Take input
s, k = input().split()
k = int(k)

# Step 2: Sort string (VERY IMPORTANT)
sorted_s = sorted(s)

# Step 3: Generate combinations with replacement
comb = combinations_with_replacement(sorted_s, k)

# Step 4: Print each combination
for c in comb:
    result = "".join(c)  # convert tuple to string
    print(result)