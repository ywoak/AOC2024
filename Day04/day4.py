import numpy as np
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
print(f'Our input as a string -> \n{test2}')

# Make into list[list[char]]
llc = [[c for c in s] for s in test2.strip().split('\n')]

print(f'\nOur input as a list[list[char]] -> ')
for lc in llc:
    print(lc)

# Observe horizontal
print('\nEach horizontal | reverse horizontal line ->')
for h in llc:
    h_std = "".join(h)
    h_rev = h_std[::-1]
    print(f'{h_std} | {h_rev}')

# Observe vertical
print('\nEach vertical | reverse vertical line ->')
for v in zip(*llc):
    v_std = "".join(v)
    v_rev = v_std[::-1]
    print(f'{v_std} | {v_rev}')

# Observe diagonals
matrix = np.array(llc)
bl_tr = [matrix[::-1,:].diagonal(i) for i in range(-matrix.shape[0]+1,matrix.shape[1])]
tl_br = [matrix.diagonal(i) for i in range(matrix.shape[1]-1,-matrix.shape[0],-1)]
print(f'BL_TR diagonals and their reverses -> {[n.tolist() for n in bl_tr]}\n')
print(f'TL_BR diagonals and their reverses -> {[n.tolist() for n in tl_br]}')
