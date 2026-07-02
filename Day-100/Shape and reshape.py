import numpy

# Read space-separated integers
numbers = list(map(int, input().split()))

# Convert list into NumPy array
array = numpy.array(numbers)

# Reshape array into 3 rows and 3 columns
array = numpy.reshape(array, (3, 3))

# Print the final array
print(array)