import sys

# Read each line from standard input (sys.stdin)
for line in sys.stdin:
    # Strip leading/trailing whitespace and split the line into words
    words = line.strip().split()
    
    # For each word in the line, output the word followed by a tab and the number 1
    for word in words:
        print(f"{word}\t1")
