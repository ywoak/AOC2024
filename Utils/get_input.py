import requests
import os
import sys

# Get day
if len(sys.argv) != 2:
    raise ValueError("Usage: python ../get_input.py <day>")
day = sys.argv[1]

#Prep requests
url = f"https://adventofcode.com/2024/day/{day}/input"
session_cookie = os.environ.get("SESSION_COOKIE")
if not session_cookie:
    raise ValueError("Required env variable: SESSION_COOKIE for input requests")
cookies = dict(session=session_cookie)

# Get data
r = requests.get(url, cookies=cookies)
if r.status_code != 200:
    raise ValueError(f"Dl issue, status: {r.status_code}")

# Write it in input file
with open(f"input.txt", "w") as file:
    file.write(r.text)
