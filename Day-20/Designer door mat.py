# Input values
n, m = map(int, input().split())

# ---------------- TOP HALF ----------------
for i in range(n // 2):
    # Step 1: Create pattern (.|.) repeated odd times
    pattern = ".|." * (2 * i + 1)

    # Step 2: Center align with '-' to total width m
    line = pattern.center(m, "-")

    # Step 3: Print line
    print(line)


# ---------------- CENTER ----------------
center_line = "WELCOME".center(m, "-")
print(center_line)


# ---------------- BOTTOM HALF ----------------
for i in range(n // 2 - 1, -1, -1):
    pattern = ".|." * (2 * i + 1)
    line = pattern.center(m, "-")
    print(line)