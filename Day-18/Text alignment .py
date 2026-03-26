# Input thickness (must be odd number)
thickness = int(input())
c = 'H'

# ---------------- TOP CONE ----------------
for i in range(thickness):
    # Left part → right aligned
    left = (c * i).rjust(thickness - 1)

    # Middle → single H
    middle = c

    # Right part → left aligned
    right = (c * i).ljust(thickness - 1)

    print(left + middle + right)


# ---------------- TOP PILLARS ----------------
for i in range(thickness + 1):
    # Two vertical blocks centered at different widths
    left_block = (c * thickness).center(thickness * 2)
    right_block = (c * thickness).center(thickness * 6)

    print(left_block + right_block)


# ---------------- MIDDLE BELT ----------------
for i in range((thickness + 1) // 2):
    # Single wide block centered
    print((c * thickness * 5).center(thickness * 6))


# ---------------- BOTTOM PILLARS ----------------
for i in range(thickness + 1):
    left_block = (c * thickness).center(thickness * 2)
    right_block = (c * thickness).center(thickness * 6)

    print(left_block + right_block)


# ---------------- BOTTOM CONE ----------------
for i in range(thickness):
    # Decreasing pattern
    left = (c * (thickness - i - 1)).rjust(thickness)
    middle = c
    right = (c * (thickness - i - 1)).ljust(thickness)

    # Entire line shifted to right
    print((left + middle + right).rjust(thickness * 6))