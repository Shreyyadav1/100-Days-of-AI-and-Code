# Step 1: Read group size
K = int(input())

# Step 2: Read room numbers
rooms = list(map(int, input().split()))

# Step 3: Create set of unique room numbers
unique_rooms = set(rooms)

# Step 4: Sum of unique room numbers
unique_sum = sum(unique_rooms)

# Step 5: Sum of all room numbers
total_sum = sum(rooms)

# Step 6: Apply formula
captain_room = (unique_sum * K - total_sum) // (K - 1)

# Step 7: Print Captain's room number
print(captain_room)