def solve(s):
    # Step 1: Split string into words
    words = s.split(" ")

    result = []

    # Step 2: Process each word
    for word in words:

        # Step 3: Check if first character is alphabet
        if word and word[0].isalpha():
            # Capitalize first letter only
            new_word = word[0].upper() + word[1:]
        else:
            # Leave unchanged
            new_word = word

        # Step 4: Add to result
        result.append(new_word)

    # Step 5: Join back with space
    return " ".join(result)


if __name__ == '__main__':
    s = input()
    print(solve(s))