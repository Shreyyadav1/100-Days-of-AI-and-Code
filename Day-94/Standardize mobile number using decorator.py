def wrapper(f):

    def fun(l):

        # Standardize every phone number
        new_list = []

        for number in l:

            # Take last 10 digits
            number = number[-10:]

            # Format number
            number = "+91 " + number[:5] + " " + number[5:]

            new_list.append(number)

        # Call sort_phone()
        f(new_list)

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)