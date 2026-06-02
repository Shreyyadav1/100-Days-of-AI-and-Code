import re

# Number of CSS lines
n = int(input())

# Read CSS code line by line
for i in range(n):

    line = input()

    # Find all valid HEX colors
    colors = re.findall(
        r'#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?',
        line
    )

    # Print colors only if line
    # belongs to CSS properties
    if ':' in line:

        for color in colors:
            print(color)