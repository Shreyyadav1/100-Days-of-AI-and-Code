from collections import defaultdict

# Step 1: Read sizes
n, m = map(int, input().split())

# Step 2: Create defaultdict (list)
word_positions = defaultdict(list)

# Step 3: Read group A and store positions
for i in range(1, n + 1):  # 1-based indexing
    word = input()

    # Store index of occurrence
    word_positions[word].append(i)

# Step 4: Process group B
for j in range(m):
    word = input()

    # Step 5: Check if word exists in group A
    if word in word_positions:
        # Print all positions
        print(*word_positions[word])
    else:
        # Print -1 if not found
        print(-1)