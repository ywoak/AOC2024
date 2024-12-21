from load_input import load_input
from custom_types import Positions
from sympy import Rational
import re

def find_goal_combination(machine: Positions) -> int:
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

def solve_equations(machine: "Positions") -> int:
    (nxA, nyA), (nxB, nyB), (gx, gy) = machine

    gx += 10000000000000
    gy += 10000000000000

    # Use rational to aovid precision error
    nxA = Rational(nxA)
    nyA = Rational(nyA)
    nxB = Rational(nxB)
    nyB = Rational(nyB)
    gx = Rational(gx)
    gy = Rational(gy)

    # Equation system of 2 with 2 unknown
    b = (gy - ((gx * nyA) / nxA)) / (nyB - ((nxB * nyA) / nxA))
    a = (gx - (b * nxB)) / nxA

    # Check for int, if 40.0 then we have the correct result, if 40.2 then no
    res = 0
    if a == int(a) and b == int(b):
        res = int(a) * 3 + int(b)
    return res

def main():
    machines: list[Positions] = [
        [
            tuple(int(coord) for coord in re.findall(r'\d+', instruction))
            for instruction in machine.split('\n')
        ]
        for machine in load_input().split("\n\n")
    ]

    part1 = 0
    part2 = 0
    for machine in machines:
        part1 += find_goal_combination(machine)
        part2 += solve_equations(machine)
    print(f"part 1: {part1}")
    print(f"part 2: {part2}")

if __name__ == "__main__":
    main()
