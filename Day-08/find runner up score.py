if __name__ == '__main__':
    n = int(input())
     # 1. Read input and convert it into a list of integers
    arr = list(map(int, input().split()))

    max_score = max(arr)

    while max_score in arr:
      arr.remove(max_score) #remove duplicate values

print(max(arr))
