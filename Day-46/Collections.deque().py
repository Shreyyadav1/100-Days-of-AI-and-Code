from collections import deque

# Step 1: Create empty deque
d = deque()

# Step 2: Number of operations
n = int(input())

# Step 3: Process each operation
for i in range(n):

    command = input().split()

    # Step 4: append
    if command[0] == "append":
        value = command[1]
        d.append(value)

    # Step 5: appendleft
    elif command[0] == "appendleft":
        value = command[1]
        d.appendleft(value)

    # Step 6: pop
    elif command[0] == "pop":
        d.pop()

    # Step 7: popleft
    elif command[0] == "popleft":
        d.popleft()

# Step 8: Print result
for item in d:
    print(item, end=" ")