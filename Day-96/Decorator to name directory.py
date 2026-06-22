import operator

def person_lister(f):

    def inner(people):

        # Step 1: Sort people by age
        people.sort(key=lambda person: int(person[2]))

        # Step 2: Store formatted names
        result = []

        # Step 3: Format names
        for person in people:
            result.append(f(person))

        # Step 4: Return result
        return result

    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')