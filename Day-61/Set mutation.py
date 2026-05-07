# Step 1: Read size of set A
n = int(input())

# Step 2: Read elements of set A
A = set(map(int, input().split()))

# Step 3: Number of operations
m = int(input())

# Step 4: Process each operation
for i in range(m):

    # Read operation name and size
    operation, size = input().split()

    # Read another set
    other_set = set(map(int, input().split()))

    # Step 5: Apply correct mutation operation

    if operation == "update":
        A.update(other_set)

    elif operation == "intersection_update":
        A.intersection_update(other_set)

    elif operation == "difference_update":
        A.difference_update(other_set)

    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(other_set)

# Step 6: Print sum of final set
print(sum(A))