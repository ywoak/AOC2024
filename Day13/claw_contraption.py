from load_input import load_input
from custom_types import Positions

import re

def find_goal_combination(machine) -> int:
    (ax, ay), (bx, by), (gx, gy) = machine
    #print(f"\n{ax, ay, bx, by, gx, gy}")

    gx += 10000000000000
    gy += 10000000000000

    #print(f"\n{ax, ay, bx, by, gx, gy}")
    upper_range: int = gx // ax
    #print(f"Upper range -> {upper_range}")
    i = upper_range
    while i > 0:
        #print(i)
        anum = gx - ax * i
        bnum: float = anum / bx
        ibnum: int = int(bnum)
        if bnum == ibnum: # and bnum <= 100: for part 1
            if (gy == (ay * i) + (by * ibnum)): # and i <= 100 and int(bnum) <= 100): for part 1
                #print(f"We have found the correct number of A and B -> {i, int(bnum)}")
                return 3 * i + int(bnum)
        i -= 1
    #print('Done 1 machine')
    return 0

def main():
    machines: list[Positions] = [
        [
            tuple(int(coord) for coord in re.findall(r'\d+', instruction))
            for instruction in machine.split('\n')
        ]
        for machine in load_input().split("\n\n")
    ]

    #print(machines)
    sum = 0
    for machine in machines:
        sum += find_goal_combination(machine)
    print(f"part 1: {sum}")

if __name__ == "__main__":
    main()
