import enum


type Position = tuple[int, int]

def parse_input() -> tuple[list[list[str]], str]:
    input: list[str] = open(0).read().strip().split('\n\n')
    map: list[list[str]] = [[char for char in line] for line in input[0].split('\n')]
    commands: str = input[1].replace("\n", "")

    return map, commands

def find_player(map: list[list[str]]) -> Position:
    for i, R in enumerate(map):
        for j, elem in enumerate(R):
            if elem == '@':
                return i, j
    return -1, -1

def execute_command(map: list[list[str]], commands: str, pos: Position):
    dirs: dict[str, Position] = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}
    for command in commands:
        dir = dirs[command]
        print(f"dir is {dir}")

def main():
    map, commands = parse_input()
    pos: Position = find_player(map)
    execute_command(map, commands, pos)

    print(map, end="\n\n")
    print(commands, end="\n\n")
    print(pos, end="\n\n")

if __name__ == "__main__":
    main()
