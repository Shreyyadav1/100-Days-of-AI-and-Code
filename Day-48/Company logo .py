from collections import Counter

if __name__ == '__main__':
    
    # Step 1: Take input ONCE
    s = input()
    
    # Step 2: Count frequency
    freq = Counter(s)
    
    # Step 3: Sort properly
    items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    
    # Step 4: Print top 3
    for i in range(3):
        print(items[i][0], items[i][1])