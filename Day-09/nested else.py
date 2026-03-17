if __name__ == '__main__':
    n = int(input())
    students = [[input(), float(input())] for _ in range(n)]

    grades = sorted({s[1] for s in students})
    second = grades[1]

    names = sorted([s[0] for s in students if s[1] == second])

    for name in names:
        print(name)