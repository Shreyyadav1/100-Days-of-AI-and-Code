n = int(input())  
# Take number of students (convert input to integer)

student_marks = {}  
# Create an empty dictionary to store data

for i in range(n):  
    # Take input line (e.g., Krishna 67 68 69) and unpack it
    # name gets the first string, line gets the remaining marks as a list
    name, *line = input().split()
    
    # Convert all strings in line to floats using a list comprehension
    marks = [float(score) for score in line]
    
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