# Enter your code here. Read input from STDIN. Print output to STDOUT
# Step 1: Read number of students (English)
n = int(input())

# Step 2: Read English subscribers
english = set(map(int, input().split()))

# Step 3: Read number of students (French)
m = int(input())

# Step 4: Read French subscribers
french = set(map(int, input().split()))

# Step 5: Find union (students with at least one subscription)
all_students = english.union(french)

# Step 6: Print total count
print(len(all_students))