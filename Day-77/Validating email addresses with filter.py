import re

# Step 1: Function to validate email
def fun(s):

    pattern = r'^[\w-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$'

    return bool(re.match(pattern, s))

# Step 2: Read number of emails
n = int(input())

emails = []

# Step 3: Store emails
for i in range(n):

    emails.append(input())

# Step 4: Filter valid emails
valid_emails = list(filter(fun, emails))

# Step 5: Sort emails lexicographically
valid_emails.sort()

# Step 6: Print result
print(valid_emails)