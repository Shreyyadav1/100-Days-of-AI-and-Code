# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

# Create custom parser
class MyHTMLParser(HTMLParser):

    # Handle comments
    def handle_comment(self, data):

        # Check single-line or multi-line
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")

        print(data)

    # Handle data
    def handle_data(self, data):

        # Ignore empty newlines
        if data.strip():
            print(">>> Data")
            print(data)

# Create parser object
parser = MyHTMLParser()

# Read number of lines
n = int(input())

# Collect HTML
html = ""

for _ in range(n):
    html += input() + "\n"

# Parse HTML
parser.feed(html)