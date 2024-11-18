#!/usr/bin/env python
import sys

current_word = None       # To keep track of the current word being processed
current_count = 0         # To keep track of the count for the current word

# Read each line from standard input (sys.stdin)
for line in sys.stdin:
    # Split the input line into the word and its count (tab-separated)
    word, count = line.strip().split('\t')
    count = int(count)    # Convert count from string to integer
    
    # If the current word matches the word in the input line, update the count
    if current_word == word:
        current_count += count
    else:
        # If the word changes (or first iteration), output the previous word and its count
        if current_word:
            print(f"{current_word}\t{current_count}")
        # Update to the new word and reset its count
        current_word = word
        current_count = count

# After the loop, output the last word and its count
if current_word == word:
    print(f"{current_word}\t{current_count}")
