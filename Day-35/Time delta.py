from datetime import datetime

# Step 1: Number of test cases
t = int(input())

# Step 2: Loop through each test case
for i in range(t):

    # Step 3: Read first timestamp
    time1_str = input()

    # Step 4: Read second timestamp
    time2_str = input()

    # Step 5: Convert string to datetime object (IMPORTANT format)
    time1 = datetime.strptime(time1_str, "%a %d %b %Y %H:%M:%S %z")
    time2 = datetime.strptime(time2_str, "%a %d %b %Y %H:%M:%S %z")

    # Step 6: Find absolute difference
    difference = abs(time1 - time2)

    # Step 7: Convert to seconds
    seconds = int(difference.total_seconds())

    # Step 8: Print result
    print(seconds)