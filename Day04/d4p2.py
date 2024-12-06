import requests
import os

# Download input
url = "https://adventofcode.com/2024/day/4/input"
session_cookie = os.environ.get("SESSION_COOKIE")
if not session_cookie:
    raise ValueError("Required env variable: SESSION_COOKIE for input requests")
cookies = dict(session=session_cookie)
r = requests.get(url, cookies=cookies)

# Make into list[list[char]]
text = r.text.strip().split('\n')
input: list[list[str]] = [[c for c in s] for s in text]

# Check ASCII values to ignore direction
def check_diagonals(tl: str, tr: str, bl: str, br: str) -> bool:
    check = ord('M') + ord('S')
    if (ord(tl) + ord(br) == check and ord(tr) + ord(bl) == check):
        return True
    return False

count = 0

# When we meet an A
# If our diagonals exist
# Verify X-MAS
for row, line in enumerate(input):
    for col, char in enumerate(line):
        if (char == 'A'):
            if (row - 1 >= 0 and row + 1 < len(input) and col - 1 >= 0 and col + 1 < len(line) and \
                check_diagonals(input[row-1][col-1], input[row-1][col+1], input[row+1][col-1], input[row+1][col+1])):
                count += 1

print(f'Number of X-MAS Occurence -> {count}')
