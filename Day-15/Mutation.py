def mutate_string(string, position, character):
    # Step 1: Take part before the index
    left_part = string[:position]

    # Step 2: Take part after the index
    right_part = string[position+1:]

    # Step 3: Combine left + new character + right
    new_string = left_part + character + right_part

    # Step 4: Return the modified string
    return new_string


if __name__ == '__main__':
    # Input original string
    s = input()

    # Input index and character
    i, c = input().split()
    i = int(i)

    # Call function and print result
    result = mutate_string(s, i, c)
    print(result)