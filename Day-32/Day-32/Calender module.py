import calendar

# Step 1: Take input
date_input = input("Enter date (DD MM YYYY or MM DD YYYY): ").strip()

# Step 2: Split input
parts = date_input.split()

# Step 3: Convert to integers
a = int(parts[0])
b = int(parts[1])
year = int(parts[2])

# Step 4: Decide which is month and which is day
# If first number > 12 → it must be day
if a > 12:
    day = a
    month = b
# If second number > 12 → it must be day
elif b > 12:
    month = a
    day = b
# If both ≤ 12 → ambiguous (default to DD MM YYYY)
else:
    day = a
    month = b

# Step 5: Get weekday
day_index = calendar.weekday(year, month, day)
day_name = calendar.day_name[day_index]

# Step 6: Print result
print("Day:", day_name.upper())