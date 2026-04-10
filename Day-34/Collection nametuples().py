from collections import namedtuple

# Step 1: Read number of students
n = int(input())

# Step 2: Read column names
columns = input().split()

# Step 3: Create namedtuple dynamically
Student = namedtuple('Student', columns)

# Step 4: Initialize total marks
total_marks = 0

# Step 5: Read each student's data
for i in range(n):

    # Take row input
    data = input().split()

    # Create Student object
    student = Student(*data)

    # Add marks (convert to int)
    total_marks += int(student.MARKS)

# Step 6: Calculate average
average = total_marks / n

# Step 7: Print with 2 decimal places
print(f"{average:.2f}")