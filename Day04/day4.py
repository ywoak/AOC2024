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

#test = "..X...\n.SAMX.\n.A..A.\nXMAS.S\n.X...." # -> 4
#test2 ="....XXMAS.\n.SAMXMS...\n...S..A...\n..A.A.MS.X\nXMASAMX.MM\nX.....XA.A\nS.S.S.S.SS\n.A.A.A.A.A\n..M.M.M.MM\n.X.X.XMASX" -> 18
#print(f'Our input as a string -> \n{test}')
#llc = [[c for c in s] for s in test.strip().split('\n')]

# Make into list[list[char]]
llc = [[c for c in s] for s in text]

print(f'\nOur input as a list[list[char]] -> ')
for lc in llc:
    print(lc)

count = 0

# Observe horizontal
print('\nEach horizontal | reverse horizontal line ->')
for h in llc:
    h_std = "".join(h)
    h_rev = h_std[::-1]
    print(f'{h_std} | {h_rev}')
    if (h_std.count("XMAS")):
        print(f"it did occur in current h_std {h_std}")
        count += h_std.count("XMAS")
    if (h_rev.count("XMAS")):
        print(f"it did occur in current h_rev {h_rev}\n")
        count += h_rev.count("XMAS")

print(f'\nCount after horizontal and reverse horizontal -> {count}')

# Observe vertical
print('\nEach vertical | reverse vertical line ->')
for v in zip(*llc):
    v_std = "".join(v)
    v_rev = v_std[::-1]
    print(f'{v_std} | {v_rev}')
    if (v_std.count("XMAS")):
        print(f"it did occur in current v_std {v_std}\n")
        count += v_std.count("XMAS")
    if (v_rev.count("XMAS")):
        print(f"it did occur in current v_rev {v_rev}\n")
        count += v_rev.count("XMAS")

print(f'\nCount after vertical and reverse vertical -> {count}')

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

print(f'\nHere are the diagonals ->\n{bl_tr_s}\n{bl_tr_rev}\n\n{tl_br_s}\n{tl_br_rev}\n')

for dbt in bl_tr_s:
    if (dbt.count("XMAS")):
        print(f"it did occur in current dbt {dbt}\n")
        count += dbt.count("XMAS")

for dtb in tl_br_s:
    if (dtb.count("XMAS")):
        print(f"it did occur in current dtb {dtb}\n")
        count += dtb.count("XMAS")

for dbt_rev in bl_tr_rev:
    if (dbt_rev.count("XMAS")):
        print(f"it did occur in current dbt_rev {dbt_rev}\n")
        count += dbt_rev.count("XMAS")

for dtb_rev in tl_br_rev:
    if (dtb_rev.count("XMAS")):
        print(f"it did occur in current dtb_rev {dtb_rev}\n")
        count += dtb_rev.count("XMAS")

print(f'Count after diagonals and reverse diagonals -> {count}')
print(f'\nNumber of XMAS Occurence -> {count}')
