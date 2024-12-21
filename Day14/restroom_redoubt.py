import re

type Robot = tuple[int, ...]
type Robots = list[Robot]

type Map = list[list[int]]

# (px, py, vx, vy) for each robot
def get_robots() -> Robots:
    input: str = open(0).read()
    return [
        tuple
        (
            int(num) for num in re.findall(r'[-]\d+|\d+', robot)
        )
        for robot in input.strip().split('\n')
    ]

def create_map() -> tuple[Map, int, int]:
    H, W = 7, 11
    map = []
    for _ in range(H):
        map.append([0] * W)
    return map, H, W

def print_map(map: Map) -> None:
    print('\n')
    for row in map:
        print(row)

def print_robots(robots: Robots) -> None:
    print('\n')
    for i, robot in enumerate(robots):
        print(f"{i} -> {robot}")

def place_robots(map: Map, robots: Robots):
    for robot in robots:
        px = robot[1]
        py = robot[0]

        map[px][py] += 1

def move_robots(map: Map, robots: Robots):
    for robot in robots:
        mx = robot[2]
        my = robot[3]
        print(f"mx -> {mx}, my -> {my}")

# px, py = position from top left 0, 0
# vx, vy = mouvement every second, positive y means right, positive x means down
# Invert x/y
# Robots wrap around the map, they teleport
# Simulte robot for initial state and 100 second (one turn = one second)
# Divide final positions in quarter, ignore middle band
# Multiply number of robot in each quarter
def simulate_robot(map: Map, robots: Robots) -> int:
    place_robots(map, robots)

    print(f"Initial position ->")
    print_map(map)

    for i in range(6):
        move_robots(map, robots)
        print(f"\nAfter {i + 1} turn ->")
        print_map(map)

    print_map(map)
    return 0

def main():
    robots = get_robots()
    map, H, W = create_map()
    print_map(map)
    print_robots(robots)
    safety_factor: int = simulate_robot(map, robots)
    print(f"part 1 : {safety_factor}")

if __name__ == '__main__':
    main()
