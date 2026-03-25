def check_string(s):
    # Step 1: Initialize all flags as False
    has_alnum = False
    has_alpha = False
    has_digit = False
    has_lower = False
    has_upper = False

    # Step 2: Traverse each character
    for ch in s:
        if ch.isalnum():
            has_alnum = True

        if ch.isalpha():
            has_alpha = True

        if ch.isdigit():
            has_digit = True

        if ch.islower():
            has_lower = True

        if ch.isupper():
            has_upper = True

    # Step 3: Print results
    print(has_alnum)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)


if __name__ == '__main__':
    s = input()
    check_string(s)