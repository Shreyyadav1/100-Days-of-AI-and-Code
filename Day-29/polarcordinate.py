import cmath

# Step 1: Take input as string
s = input()

# Step 2: Convert string to complex number
z = complex(s)

# Step 3: Calculate modulus (distance from origin)
modulus = abs(z)

# Step 4: Calculate phase angle
angle = cmath.phase(z)

# Step 5: Print results
print(modulus)
print(angle)