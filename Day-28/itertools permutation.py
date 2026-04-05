from itertools import permutations

# Step 1: Take input
s, k = input().split()
k = int(k)

# Step 2: Sort the string (VERY IMPORTANT)
sorted_s = sorted(s)

# Step 3: Generate permutations
perm = permutations(sorted_s, k)

# Step 4: Print each permutation
for p in perm:
    # Convert tuple to string
    result = "".join(p)
    print(result)