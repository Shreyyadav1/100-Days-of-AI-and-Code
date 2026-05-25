import re

# Step 1: Read string
s = input()

# Step 2: Search for consecutive repeating
# alphanumeric characters
match = re.search(r'([a-zA-Z0-9])\1', s)

# Step 3: Print result
if match:

    # group(1) gives repeating character
    print(match.group(1))

else:
    print(-1)