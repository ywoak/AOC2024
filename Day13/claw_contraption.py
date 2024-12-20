from load_input import load_input
import re

def main():
    machines = [
        [
            tuple(int(coord) for coord in re.findall(r'\d+', instruction))
            for instruction in machine.split('\n')
        ]
        for machine in load_input().split("\n\n")
    ]

    print(machines)
    for machine in machines:
        print(f"\n{machine}")

if __name__ == "__main__":
    main()
