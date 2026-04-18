import re

# Step 1: Read number of test cases
t = int(input())

# Step 2: Loop through each test case
for i in range(t):

    # Step 3: Read regex pattern
    pattern = input()

    try:
        # Step 4: Try compiling regex
        re.compile(pattern)

        # Step 5: If no error → valid
        print("True")

    except re.error:
        # Step 6: If error occurs → invalid
        print("False")