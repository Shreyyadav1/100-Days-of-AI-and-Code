from collections import Counter

# Step 1: Number of shoes (not really needed, but part of input)
n = int(input())

# Step 2: Read shoe sizes
sizes = list(map(int, input().split()))

# Step 3: Create counter (size → count)
shoe_count = Counter(sizes)

# Step 4: Number of customers
customers = int(input())

# Step 5: Initialize total earnings
total_money = 0

# Step 6: Process each customer
for i in range(customers):

    # Input desired size and price
    size, price = map(int, input().split())

    # Step 7: Check if shoe available
    if shoe_count[size] > 0:

        # Sell shoe → add money
        total_money += price

        # Reduce stock
        shoe_count[size] -= 1

    # Else → do nothing (no stock)

# Step 8: Print total earnings
print(total_money)