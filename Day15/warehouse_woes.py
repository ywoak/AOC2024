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
                elem = '.'
                return i, j
    return -1, -1

def execute_command(map: list[list[str]], commands: str, pos: Position):
    x, y = pos

    dirs: dict[str, Position] = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}
    for command in commands:
        dx, dy = dirs[command]
        print(f"dir is {dir}")
        # get command
        # on regarde dans la bonne direction, si c'est un point on avance
        # Si c'est un obstacle on les depasse, si c'est un point apres on switch
        # Si c'est un mur on passe a la commande suivante
        nx, ny = inx, iny = x + dx, y + dy
        obstacle = False
        while (map[nx][ny] == 'O'):
            nx += 1
            ny += 1
            obstacle = True
        if (map[nx][ny] == '#'): continue
        if obstacle:
            map[nx][ny] = 'O'
            map[inx][iny] = '@'
            map[x][y] = '.'
            obstacle = False

        x, y = inx, iny

def main():
    map, commands = parse_input()
    pos: Position = find_player(map)
    execute_command(map, commands, pos)
    #get_gps_score(map)

    print(map, end="\n\n")
    print(commands, end="\n\n")
    print(pos, end="\n\n")

if __name__ == "__main__":
    main()
