type Map = list[list[str]]
type Command = str

type Position = tuple[int, int]
type Positions = list[Position]

def parse_input() -> tuple[Map, Command]:
    input: list[str] = open(0).read().strip().split('\n\n')
    map: Map = [[char for char in line] for line in input[0].split('\n')]
    commands: Command = input[1].replace("\n", "")

    return map, commands

def find_player(map: Map) -> Position:
    for i, R in enumerate(map):
        for j, elem in enumerate(R):
            if elem == '@':
                elem = '.'
                return i, j
    return -1, -1

def execute_command(map: Map, commands: Command, pos: Position):
    x, y = pos

    dirs: dict[str, Position] = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}
    for command in commands:
        dx, dy = dirs[command]
        nx, ny = inx, iny = x + dx, y + dy
        obstacle = False
        while (map[nx][ny] == 'O'):
            nx += dx
            ny += dy
            obstacle = True
        if (map[nx][ny] == '#'): continue
        if obstacle:
            map[nx][ny] = 'O'
            obstacle = False

        map[x][y] = '.'
        map[inx][iny] = '@'
        x, y = inx, iny

def get_gps_score(map: Map) -> int:
    score: int = 0
    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] == 'O':
                score += 100 * x + y
    return score

def main():
    map, commands = parse_input()
    pos: Position = find_player(map)

    execute_command(map, commands, pos)
    score: int = get_gps_score(map)

    print(f"Part 1: {score}")

if __name__ == "__main__":
    main()
