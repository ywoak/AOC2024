import re

type Robot = tuple[int, int, int, int]
type Robots = list[Robot]

type Map = list[list[int]]

# px, py = position from top left 0, 0
# vx, vy = mouvement every second, positive y means right, positive x means down
def get_robots() -> Robots:
    input: str = open(0).read()
    return [
        tuple(
            num for num in re.findall(r'[-]\d+|\d+', robot)
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
        px = int(robot[1])
        py = int(robot[0])

        map[px][py] += 1

# Robots wrap around the map, they teleport
# Invert x/y
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
