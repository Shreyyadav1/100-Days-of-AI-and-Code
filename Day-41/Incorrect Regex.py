import re

t = int(input())

for _ in range(t):
    pattern = input()
    
    try:
        re.compile(pattern)
        
        # Reject invalid consecutive quantifiers (except escaped ones)
        if re.search(r'(?<!\\)[\*\+\?]{2,}', pattern):
            print("False")
        else:
            print("True")
            
    except re.error:
        print("False")