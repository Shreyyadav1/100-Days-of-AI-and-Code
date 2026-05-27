import re

# Step 1: Read string
s = input()

# Step 2: Regex pattern
pattern = r'(?<=[^aeiouAEIOU\W\d_])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU\W\d_])'

# Step 3: Find all matches
matches = re.findall(pattern, s)

# Step 4: Print matches
if matches:

    for i in matches:
        print(i)

else:
    print(-1)