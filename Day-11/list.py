if __name__ == '__main__':
    n = int(input())  # number of commands
    lst = []          # empty list

    for _ in range(n):
        cmd = input().split()  # take command and split into parts

        if cmd[0] == "insert":
            # insert element at given position
            lst.insert(int(cmd[1]), int(cmd[2]))

        elif cmd[0] == "print":
            # print the list
            print(lst)

        elif cmd[0] == "remove":
            # remove first occurrence of element
            lst.remove(int(cmd[1]))

        elif cmd[0] == "append":
            # add element at the end
            lst.append(int(cmd[1]))

        elif cmd[0] == "sort":
            # sort the list in ascending order
            lst.sort()

        elif cmd[0] == "pop":
            # remove last element
            lst.pop()

        elif cmd[0] == "reverse":
            # reverse the list
            lst.reverse()