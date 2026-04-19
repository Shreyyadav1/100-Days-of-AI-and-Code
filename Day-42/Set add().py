# Step 1: Read number of stamps
n = int(input())

# Step 2: Create empty set
country_stamps = set()

# Step 3: Add each country to set
for i in range(n):
    country = input()
    country_stamps.add(country)

# Step 4: Count unique countries
distinct_count = len(country_stamps)

# Step 5: Print result
print(distinct_count)