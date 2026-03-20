if __name__ == '__main__':
    # Take number of elements (not really needed but given in question)
    n = int(input())

    # Take space-separated integers and convert into tuple
    t = tuple(map(int, input().split()))

    # Print hash of tuple
    print(hash(t))