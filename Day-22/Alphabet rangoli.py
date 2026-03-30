def print_rangoli(size):
    # Step 1: Alphabet string
    alpha = "abcdefghijklmnopqrstuvwxyz"

    # Step 2: Total width of pattern
    width = 4 * size - 3

    # ---------------- TOP HALF ----------------
    for i in range(size - 1, -1, -1):

        # Step 3: Left side (reverse part)
        left = alpha[size-1:i:-1]

        # Step 4: Right side
        right = alpha[i:size]

        # Step 5: Combine both sides
        full = left + right

        # Step 6: Join with '-'
        line = "-".join(full)

        # Step 7: Center align
        print(line.center(width, "-"))

    # ---------------- BOTTOM HALF ----------------
    for i in range(1, size):

        left = alpha[size-1:i:-1]
        right = alpha[i:size]
        full = left + right
        line = "-".join(full)

        print(line.center(width, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)