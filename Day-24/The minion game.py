def minion_game(string):
    # Step 1: Define vowels
    vowels = "AEIOU"

    # Step 2: Initialize scores
    kevin_score = 0
    stuart_score = 0

    # Step 3: Length of string
    n = len(string)

    # Step 4: Traverse string
    for i in range(n):

        # Number of substrings starting from index i
        score = n - i

        # Step 5: Check if vowel or consonant
        if string[i] in vowels:
            # Kevin gets points
            kevin_score += score
        else:
            # Stuart gets points
            stuart_score += score

    # Step 6: Decide winner
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)