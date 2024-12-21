import re

# [px, py, vx, vy] for each robot
type Robot = list[int]
type Robots = list[Robot]

type Map = list[list[int]]

def get_robots() -> Robots:
    input: str = open(0).read()
    return [
        [
            int(num) for num in re.findall(r'[-]\d+|\d+', robot)
        ]
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
        px = robot[0]
        py = robot[1]

        map[py][px] += 1

def move_robots(map: Map, robots: Robots, H: int, W: int):
    for robot in robots:
        px, py, mx, my = robot

        # Calculate end position for a turn while wrapping
        nx, ny = (px + mx) % W, (py + my) % H
        #print(f"px -> {px}, py -> {py}, mx -> {mx}, my -> {my}, nx {nx}, ny {ny}")

        # Move robot
        map[py][px] -= 1
        map[ny][nx] += 1

        # Update robot
        robot[0] = nx
        robot[1] = ny

def get_quarters(map: Map, H: int, W: int) -> tuple[Map, Map, Map, Map]:
    first_quarter = [half_row[:W // 2] for half_row in map[:H // 2]]
    second_quarter = [half_row[W // 2 + 1:] for half_row in map[:H // 2]]
    third_quarter = [half_row[:W // 2] for half_row in map[H // 2 + 1:]]
    fourth_quarter = [half_row[W // 2 + 1:] for half_row in map[H // 2 + 1:]]
    return first_quarter, second_quarter, third_quarter, fourth_quarter

# px, py = position from top left 0, 0
# vx, vy = mouvement every second, positive y means right, positive x means down
# Invert x/y
# Robots wrap around the map, they teleport
# Simulte robot for initial state and 100 second (one turn = one second)
# Divide final positions in quarter, ignore middle band
# Multiply number of robot in each quarter
#
# We mutate robot to hold current positions
def simulate_robot(map: Map, robots: Robots, H: int, W: int) -> int:
    place_robots(map, robots)

    print(f"Initial robots position ->")
    print_map(map)

    for i in range(100):
        move_robots(map, robots, H, W)

        print(f"\nAfter {i + 1} turn ->")
        print_map(map)

    quarters: tuple[Map, Map, Map, Map] = get_quarters(map, H, W)
    result = get_results()
    for quarter in quarters:
        x, y = 0, 0

        print(f"quarter -> {quarter}")

    return result

def main():
    robots = get_robots()
    map, H, W = create_map()
    print('initial map ->')
    print_map(map)
    print('initial robots ->')
    print_robots(robots)
    safety_factor: int = simulate_robot(map, robots, H, W)
    print(f"part 1 : {safety_factor}")

if __name__ == '__main__':
    main()
