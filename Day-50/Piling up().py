from collections import deque

# Step 1: Number of test cases
t = int(input())

for i in range(t):

    # Step 2: Number of cubes
    n = int(input())

    # Step 3: Create deque (for left/right access)
    cubes = deque(map(int, input().split()))

    # Step 4: Initialize last placed cube (very large)
    last = float('inf')

    # Step 5: Process cubes
    while cubes:

        # Step 6: Pick larger of two ends
        if cubes[0] >= cubes[-1]:
            chosen = cubes.popleft()
        else:
            chosen = cubes.pop()

        # Step 7: Check stacking rule
        if chosen > last:
            print("No")
            break

        # Step 8: Update last placed cube
        last = chosen

    else:
        # Step 9: If loop completes successfully
        print("Yes")