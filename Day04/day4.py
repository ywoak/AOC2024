import requests
import os

url = "https://adventofcode.com/2024/day/4/input"
session_cookie = os.environ.get("SESSION_COOKIE")
if not session_cookie:
    raise ValueError("Required env variable: SESSION_COOKIE for input requests")
cookies = dict(session=session_cookie)
r = requests.get(url, cookies=cookies)

r.text.strip()
