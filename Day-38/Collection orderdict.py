from collections import OrderedDict

# Step 1: Number of items
n = int(input())

# Step 2: Create ordered dictionary
items = OrderedDict()

# Step 3: Process each entry
for i in range(n):

    # Step 4: Split input
    data = input().split()

    # Step 5: Last value is price
    price = int(data[-1])

    # Step 6: Remaining is item name
    item_name = " ".join(data[:-1])

    # Step 7: Add or update price
    if item_name in items:
        items[item_name] += price
    else:
        items[item_name] = price

# Step 8: Print result
for name, total_price in items.items():
    print(name, total_price)