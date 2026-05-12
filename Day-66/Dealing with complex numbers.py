import math

class Complex:

    # Constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Addition
    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return Complex(real, imag)

    # Subtraction
    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return Complex(real, imag)

    # Multiplication
    def __mul__(self, other):
        real = (self.real * other.real) - (self.imag * other.imag)
        imag = (self.real * other.imag) + (self.imag * other.real)
        return Complex(real, imag)

    # Division
    def __truediv__(self, other):

        denominator = (other.real ** 2) + (other.imag ** 2)

        real = ((self.real * other.real) +
                (self.imag * other.imag)) / denominator

        imag = ((self.imag * other.real) -
                (self.real * other.imag)) / denominator

        return Complex(real, imag)

    # Modulus
    def mod(self):
        value = math.sqrt((self.real ** 2) + (self.imag ** 2))
        return Complex(value, 0)

    # String formatting
    def __str__(self):

        if self.imag == 0:
            return "%.2f+0.00i" % self.real

        elif self.real == 0:

            if self.imag >= 0:
                return "0.00+%.2fi" % self.imag
            else:
                return "0.00-%.2fi" % abs(self.imag)

        else:

            if self.imag >= 0:
                return "%.2f+%.2fi" % (self.real, self.imag)
            else:
                return "%.2f-%.2fi" % (self.real, abs(self.imag))


# Input
real1, imag1 = map(float, input().split())
real2, imag2 = map(float, input().split())

# Create objects
C = Complex(real1, imag1)
D = Complex(real2, imag2)

# Print operations
print(C + D)
print(C - D)
print(C * D)
print(C / D)
print(C.mod())
print(D.mod())