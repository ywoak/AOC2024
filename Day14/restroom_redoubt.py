import re

type Robot = list[int]
type Robots = list[Robot]

type Map = list[list[int]]
type Quarter = Map
type Quarters = tuple[Quarter, Quarter, Quarter, Quarter]

# Global to re use for part2
input: str = open(0).read()

def get_robots() -> Robots:
    """
    Get data for each robot:
    [px, py, vx, vy]
    """
    return [
        [
            int(num) for num in re.findall(r'[-]\d+|\d+', robot)
        ]
        for robot in input.strip().split('\n')
    ]

def create_map() -> tuple[Map, int, int]:
    """
    Initial creation of the map
    H, W for test -> 7, 11
    H, W for input -> 103, 101
    """
    #H, W = 7, 11
    H, W = 103, 101
    map = []
    for _ in range(H):
        map.append([0] * W)
    return map, H, W

def print_map(map: Map) -> None:
    """
    Fonction to print the map
    We use it to display the easter egg
    """
    for row in map:
        print(row)
    print('\n')

def print_robots(robots: Robots) -> None:
    """ Debugging fonction to print robots """
    print('\n')
    for i, robot in enumerate(robots):
        print(f"{i} -> {robot}")

def place_robots(map: Map, robots: Robots) -> None:
    """ Initial placement of the robot """
    for robot in robots:
        px = robot[0]
        py = robot[1]

        map[py][px] += 1

def move_robots(map: Map, robots: Robots, H: int, W: int) -> None:
    """
    0. Get info for each robot
    1. Find robot path while taking wrapping into account
    2. Move the robot in the map, remove where it was, add where it is
    3. We mutate robot to hold current positions
    """
    for robot in robots:
        px, py, mx, my = robot

        nx, ny = (px + mx) % W, (py + my) % H

        map[py][px] -= 1
        map[ny][nx] += 1

        robot[0] = nx
        robot[1] = ny

def get_quarters(map: Map, H: int, W: int) -> Quarters:
    """ Divide final positions in quarters, ignore middle band """
    first_quarter: Quarter = [half_row[:W // 2] for half_row in map[:H // 2]]
    second_quarter: Quarter = [half_row[W // 2 + 1:] for half_row in map[:H // 2]]
    third_quarter: Quarter = [half_row[:W // 2] for half_row in map[H // 2 + 1:]]
    fourth_quarter: Quarter = [half_row[W // 2 + 1:] for half_row in map[H // 2 + 1:]]

    return first_quarter, second_quarter, third_quarter, fourth_quarter

def get_safety_factor(quarters: Quarters) -> int:
    """ Multiply number of robots in each quarter """
    safety_factor = 1

    for quarter in quarters:
        sum_quarter = 0
        for R in quarter:
            for elem in R:
                sum_quarter += elem

        safety_factor *= sum_quarter

    return safety_factor

def is_easter_egg(map: Map) -> bool:
    """
    We eventually have an easter egg for part 2
    The robots positions will display a tree shape
    We dont actually need to check for the shape of a tree, its the only time where the robots each has a unique position

    (That's not true for the tests cases, its only true for the actual robots)
    """
    for R in map:
        for tile in R:
            if (tile >= 2):
                return False
    return True

def simulate_robot(map: Map, robots: Robots, H: int, W: int, part2: bool) -> int:
    """
    Simulate the evolution of the robot in their map (1 loop turn = 1 second)
    For part1 simulate 100s, get quarters, and get the safety factor out of them
    For part2 simulate until we meet the easter egg, a tree shape
    """
    place_robots(map, robots)

    if part2:
        for i in range(10000):
            move_robots(map, robots, H, W)

            if (is_easter_egg(map)):
                print_map(map)
                return i + 1
    else:
        for i in range(100):
            move_robots(map, robots, H, W)

    quarters: Quarters = get_quarters(map, H, W)
    safety_factor: int = get_safety_factor(quarters)

    return safety_factor

def main():
    map, H, W = create_map()
    robots: Robots = get_robots()
    safety_factor: int = simulate_robot(map, robots, H, W, part2=False)

    map, H, W = create_map()
    robots: Robots = get_robots()
    easter_egg_seconds: int = simulate_robot(map, robots, H, W, part2=True)

    print(f"part 1: {safety_factor}")
    print(f"Part 2: {easter_egg_seconds}")

if __name__ == '__main__':
    main()
