if __name__ == '__main__':
    print("System Online. (Exit hone ke liye '0' dabayein)")

    # CHANGE 1: Yahan loop shuru ho raha hai
    while True:
        n_input = input("Enter number: ").strip()
        n = int(n_input)

        # CHANGE 2: Exit condition (taaki program band bhi ho sake)
        if n == 0:
            print("Exiting...")
            break

        # CHANGE 3: Tumhara puraana logic ab loop ke andar (Thoda aage khisaka hua)
        if n % 2 != 0:
            print("Weird")
        elif n >= 2 and n <= 5:
            print("Not Weird")
        elif n >= 6 and n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")