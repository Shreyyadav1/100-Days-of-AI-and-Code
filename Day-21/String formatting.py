def print_formatted(number):
    # Step 1: Find width using binary of max number
    width = len(bin(number)) - 2   # remove '0b'

    # Step 2: Loop from 1 to number
    for i in range(1, number + 1):

        # Step 3: Convert to different formats
        decimal = str(i)
        octal = oct(i)[2:]        # remove '0o'
        hexa = hex(i)[2:].upper() # remove '0x' and capitalize
        binary = bin(i)[2:]       # remove '0b'

        # Step 4: Right align all values
        decimal = decimal.rjust(width)
        octal = octal.rjust(width)
        hexa = hexa.rjust(width)
        binary = binary.rjust(width)

        # Step 5: Print in one line
        print(decimal, octal, hexa, binary)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)