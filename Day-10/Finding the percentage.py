n = int(input())  
# Take number of students (convert input to integer)

student_marks = {}  
# Create an empty dictionary to store data

for i in range(n):  
    data = input().split()  
    # Take input like: Krishna 67 68 69 → split into list

    name = data[0]  
    # First item is the name

    marks = list(map(float,data[1:]))
    # Remaining items are marks → convert them into numbers

    student_marks[name] = marks  
    # Store name and marks in dictionary

query_name = input()  
# Take the name we want to search

marks_list = student_marks[query_name]  
# Get marks of that student

average = sum(marks_list) / len(marks_list)  
# Calculate average

print(f"{average:.2f}")  
# Print answer with 2 decimal places