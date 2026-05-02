# Enter your code here. Read input from STDIN. Print output to STDOUT
# Step 1: Take inputs
a = int(input())
b = int(input())
m = int(input())

# Step 2: Calculate power (a^b)
power_result = pow(a, b)

# Step 3: Calculate modular power (a^b % m)
mod_result = pow(a, b, m)

# Step 4: Print results
print(power_result)
print(mod_result)