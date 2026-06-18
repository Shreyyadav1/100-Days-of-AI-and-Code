import re

# Read number of test cases
n = int(input())

# Process each credit card
for i in range(n):

    # Read credit card number
    card = input()

    # Condition 1:
    # Must start with 4, 5 or 6
    # Must contain exactly 16 digits
    # Hyphens are allowed only in groups of 4 digits
    pattern = r'^[456]\d{3}(-?\d{4}){3}$'

    if not re.match(pattern, card):
        print("Invalid")
        continue

    # Remove hyphens
    number = card.replace("-", "")

    # Condition 2:
    # No digit should repeat 4 or more times consecutively
    if re.search(r'(\d)\1\1\1', number):
        print("Invalid")
        continue

    # All conditions satisfied
    print("Valid")