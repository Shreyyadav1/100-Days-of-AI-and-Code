import re

# Step 1: Read main string
s = input()

# Step 2: Read substring
k = input()

# Step 3: Find overlapping matches
matches = list(re.finditer(r'(?={})'.format(k), s))

# Step 4: Print indices
if matches:

    for match in matches:

        start = match.start()

        end = start + len(k) - 1

        print((start, end))

else:
    print((-1, -1))