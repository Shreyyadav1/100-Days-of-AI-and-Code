# Step 1: Read size of set A
m = int(input())

# Step 2: Read elements of set A
A = set(map(int, input().split()))

# Step 3: Read size of set B
n = int(input())

# Step 4: Read elements of set B
B = set(map(int, input().split()))

# Step 5: Find symmetric difference
# Elements in A or B but not both
result = A.symmetric_difference(B)

# Step 6: Sort the result
sorted_result = sorted(result)

# Step 7: Print each element
for num in sorted_result:
    print(num)