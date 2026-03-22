def split_and_join(line):
    # Step 1: Split the string into words
    # IMPORTANT: separator must NOT be ""
    words = line.split()  

    # Step 2: Join using hyphen
    result = "-".join(words)

    # Step 3: Return result
    return result


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)