def wrap(string, max_width):
    # Step 1: Create empty list to store parts
    result = []

    # Step 2: Loop in steps of max_width
    for i in range(0, len(string), max_width):
        # Step 3: Take substring of size max_width
        part = string[i:i + max_width]

        # Step 4: Add to list
        result.append(part)

    # Step 5: Join with newline
    final_output = "\n".join(result)

    # Step 6: Return result
    return final_output


if __name__ == '__main__':
    string = input()
    max_width = int(input())

    output = wrap(string, max_width)
    print(output)