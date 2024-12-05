import requests
import os

url = "https://adventofcode.com/2024/day/4/input"
session_cookie = os.environ.get("SESSION_COOKIE")
if not session_cookie:
    raise ValueError("Required env variable: SESSION_COOKIE for input requests")
cookies = dict(session=session_cookie)
r = requests.get(url, cookies=cookies)

#print(r.text.strip().split('\n'))

test = "SBBSBBS\nBABABAB\nBBMMMBB\nSAMXMAS\nBBMMMBB\nBABABAB\nSBBSBBS\n"

test2 = "..X...\n.SAMX.\n.A..A.\nXMAS.S\n.X...."
print(test2)

a = [[c for c in s] for s in test2.strip().split('\n')]

for i in a:
    print(i)
