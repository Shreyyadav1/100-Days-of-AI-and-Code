from collections import OrderedDict

# Step 1: Read number of words
n = int(input())

# Step 2: Create ordered dictionary
word_count = OrderedDict()

# Step 3: Read each word
for i in range(n):
    word = input()

    # Step 4: Count occurrences
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Step 5: Print number of distinct words
print(len(word_count))

# Step 6: Print counts in order
for count in word_count.values():
    print(count, end=" ")