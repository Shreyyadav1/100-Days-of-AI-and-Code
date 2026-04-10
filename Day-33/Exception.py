# Step 1: Read number of test cases
t = int(input())

# Step 2: Loop through each test case
for i in range(t):

    # Step 3: Take input values (as strings)
    a, b = input().split()

    try:
        # Step 4: Convert to integers
        num1 = int(a)
        num2 = int(b)

        # Step 5: Perform integer division
        result = num1 // num2

        # Step 6: Print result
        print(result)

    except ZeroDivisionError as e:
        # Step 7: Handle division by zero
        print("Error Code:", e)

    except ValueError as e:
        # Step 8: Handle invalid integer conversion
        print("Error Code:", e)