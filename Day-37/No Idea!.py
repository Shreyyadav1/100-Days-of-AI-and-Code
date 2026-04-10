# Step 1: Read n and m
n, m = map(int, input().split())

# Step 2: Read array
arr = list(map(int, input().split()))

# Step 3: Read set A (liked numbers)
set_A = set(map(int, input().split()))

# Step 4: Read set B (disliked numbers)
set_B = set(map(int, input().split()))

# Step 5: Initialize happiness
happiness = 0

# Step 6: Traverse array
for num in arr:

    # Step 7: Check if in A
    if num in set_A:
        happiness += 1

    # Step 8: Check if in B
    if num in set_B:
        happiness -= 1

# Step 9: Print result
print(happiness)