from itertools import combinations

# Step 1: Read input
n = int(input())
letters = input().split()
k = int(input())

# Step 2: Generate all possible index combinations
all_combinations = list(combinations(range(n), k))

# Step 3: Count favorable cases (at least one 'a')
favorable = 0

for comb in all_combinations:
    
    # Check if any index in this combination has 'a'
    has_a = False
    for index in comb:
        if letters[index] == 'a':
            has_a = True
            break

    if has_a:
        favorable += 1

# Step 4: Total cases
total = len(all_combinations)

# Step 5: Probability
probability = favorable / total

# Step 6: Print result
print(probability)