# Function to swap case of each character
def swap_case(s):
    result = ""   # empty string to store final result

    # Loop through each character in the string
    for ch in s:
        
        # If character is lowercase → convert to uppercase
        if ch.islower():
            result += ch.upper()
        
        # If character is uppercase → convert to lowercase
        elif ch.isupper():
            result += ch.lower()
        
        # If it's not a letter (number, space, symbol) → keep same
        else:
            result += ch

    return result   # return final modified string


# Main program starts here
if __name__ == '__main__':
    s = input()                 # take input from user
    print(swap_case(s))         # call function and print result