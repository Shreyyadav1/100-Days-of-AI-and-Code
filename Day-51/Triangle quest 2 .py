# Step 1: Take input (size of triangle)
n = int(input())

# Step 2: Loop from 1 to n
for i in range(1, n + 1):

    # Step 3: Create number with repeated 1's
    # Example: i=3 → 111
    base_number = (10 ** i) // 9

    # Step 4: Square it to form palindrome
    # Example: 111^2 → 12321
    palindrome = base_number ** 2

    # Step 5: Print result
    print(palindrome)