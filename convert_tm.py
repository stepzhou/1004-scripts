import re
import sys

def convert(tm_string):
    # replace state 1 with starting state 0
    tm_string = re.sub(r'(\d+ \w+ \w+) 1 ([rl])', r'\1 0 \2', tm_string)
    tm_string = re.sub(r'1 (\w+ \w+ \w+ \w+)', r'0 \1', tm_string)
    # switch last 2 elements
    tm_string = re.sub(r'(\d+) ([rl])', r'\2 \1', tm_string)
    # replace b with _
    tm_string = re.sub(r'b', r'_', tm_string)
    return tm_string

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        for line in f:
            print convert(line.strip())
