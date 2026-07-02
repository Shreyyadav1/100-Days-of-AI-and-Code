# pyrefly: ignore [missing-import]
import numpy


def arrays(arr):

    # Convert list into NumPy array of float type
    arr = numpy.array(arr, float)

    # Reverse the array
    arr = arr[::-1]

    # Return reversed array
    return arr


if __name__ == "__main__":
    # Take space-separated numbers as input
    user_input = input("Enter numbers separated by spaces: ")
    arr = list(map(float, user_input.split()))
    result = arrays(arr)
    print(result)