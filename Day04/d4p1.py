import numpy as np
import requests
import os

url = "https://adventofcode.com/2024/day/4/input"
session_cookie = os.environ.get("SESSION_COOKIE")
if not session_cookie:
    raise ValueError("Required env variable: SESSION_COOKIE for input requests")
cookies = dict(session=session_cookie)
r = requests.get(url, cookies=cookies)

text = r.text.strip().split('\n')

# Make into list[list[char]]
llc = [[c for c in s] for s in text]

count = 0

# Observe horizontal
for h in llc:
    h_std = "".join(h)
    h_rev = h_std[::-1]
    if (h_std.count("XMAS")):
        count += h_std.count("XMAS")
    if (h_rev.count("XMAS")):
        count += h_rev.count("XMAS")

# Observe vertical
for v in zip(*llc):
    v_std = "".join(v)
    v_rev = v_std[::-1]
    if (v_std.count("XMAS")):
        count += v_std.count("XMAS")
    if (v_rev.count("XMAS")):
        count += v_rev.count("XMAS")

# Observe diagonals
matrix = np.array(llc)
bl_tr_a = [matrix[::-1,:].diagonal(i) for i in range(-matrix.shape[0]+1,matrix.shape[1])]
tl_br_a = [matrix.diagonal(i) for i in range(matrix.shape[1]-1,-matrix.shape[0],-1)]
bl_tr_l = ([n.tolist() for n in bl_tr_a])
tl_br_l = ([n.tolist() for n in tl_br_a])
bl_tr_s = ["".join(el) for el in bl_tr_l]
tl_br_s = ["".join(el) for el in tl_br_l]
bl_tr_rev = [el[::-1] for el in bl_tr_s]
tl_br_rev =  [el[::-1] for el in tl_br_s]

for dbt in bl_tr_s:
    if (dbt.count("XMAS")):
        count += dbt.count("XMAS")

for dtb in tl_br_s:
    if (dtb.count("XMAS")):
        count += dtb.count("XMAS")

for dbt_rev in bl_tr_rev:
    if (dbt_rev.count("XMAS")):
        count += dbt_rev.count("XMAS")

for dtb_rev in tl_br_rev:
    if (dtb_rev.count("XMAS")):
        count += dtb_rev.count("XMAS")

print(f'Number of XMAS Occurence -> {count}')
