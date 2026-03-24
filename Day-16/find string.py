def count_substring(string, sub_string):
    # Step 1: Initialize counter
    count = 0

    # Step 2: Loop through valid starting positions
    # We stop early to avoid index error
    for i in range(0, len(string) - len(sub_string) + 1):

        # Step 3: Extract part of string equal to substring length
        part = string[i:i + len(sub_string)]

        # Step 4: Compare with substring
        if part == sub_string:
            count += 1

    # Step 5: Return total count
    return count


if __name__ == '__main__':
    # Input main string
    string = input()

    # Input substring
    sub_string = input()

    # Call function and print result
    result = count_substring(string, sub_string)
    print(result)