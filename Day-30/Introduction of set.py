def average(arr):
    # Step 1: Remove duplicates using set
    unique_heights = set(arr)

    # Step 2: Calculate sum of unique values
    total = sum(unique_heights)

    # Step 3: Count number of unique values
    count = len(unique_heights)

    # Step 4: Calculate average
    avg = total / count

    # Step 5: Return result
    return avg


if __name__ == '__main__':
    # Input size (not really needed for logic)
    n = int(input())

    # Input list of heights
    arr = list(map(int, input().split()))

    # Call function
    result = average(arr)

    # Print result
    print(result)