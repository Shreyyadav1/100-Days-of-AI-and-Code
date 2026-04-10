import math

# Step 1: Input
AB = int(input())
BC = int(input())

# Step 2: Calculate angle
angle_radians = math.atan(AB / BC)

# Step 3: Convert to degrees
angle_degrees = math.degrees(angle_radians)

# Step 4: Round value
final_angle = round(angle_degrees)

# Step 5: Print with degree symbol (ASCII-safe)
degree_symbol = chr(176)
print(str(final_angle) + degree_symbol)