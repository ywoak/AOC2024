from load_input import load_input
from custom_types import Positions

import re

def find_goal_combination(machine) -> int:
    (ax, ay), (bx, by), (gx, gy) = machine

    upper_range: int = gx // ax
    i = upper_range
    while i > 0:
        anum = gx - ax * i
        bnum: float = anum / bx
        ibnum: int = int(bnum)
        if bnum == ibnum and bnum <= 100:
            if (gy == (ay * i) + (by * ibnum) and i <= 100 and int(bnum) <= 100):
                return 3 * i + int(bnum)
        i -= 1
    return 0

def main():
    machines: list[Positions] = [
        [
            tuple(int(coord) for coord in re.findall(r'\d+', instruction))
            for instruction in machine.split('\n')
        ]
        for machine in load_input().split("\n\n")
    ]

    sum = 0
    for machine in machines:
        sum += find_goal_combination(machine)
    print(f"part 1: {sum}")

if __name__ == "__main__":
    main()
