from itertools import combinations

# Step 1: Take input
s, k = input().split()
k = int(k)

# Step 2: Sort string (VERY IMPORTANT)
sorted_s = sorted(s)

# Step 3: Loop from size 1 to k
for size in range(1, k + 1):

    # Step 4: Generate combinations of current size
    comb = combinations(sorted_s, size)

    # Step 5: Print each combination
    for c in comb:
        result = "".join(c)  # convert tuple to string
        print(result)