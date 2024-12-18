from collections import defaultdict

type Stone = str
type Stones = list[Stone]

type Count = defaultdict[Stone, int]

def load_map():
    with open('input.txt') as f:
        input = f.read()
    return [c for c in input.strip().split(' ')]

def blink(count: Count) -> Count:
    cpy: Count = defaultdict(int)

    for stone, val in count.items():
        length = len(stone)

        if (stone == '0'):
            tmp: Stones = [str(1)]
        elif (length % 2 == 0):
            tmp: Stones = [stone[:length//2], str(int(stone[length//2:]))]
        else:
            tmp: Stones = [str(int(stone) * 2024)]

        for next in tmp:
            cpy[next] += val
    return cpy

def fill_cache(stones: Stones, count_cache: Count) -> Count:
    for stone in stones:
        count_cache[stone] += 1
    return count_cache

def main():
    stones: Stones = load_map()
    count: Count = defaultdict(int)
    count = fill_cache(stones, count)

    for i in range(75):
        count = blink(count)
        if i == 24:
            print(f"Part 1: {sum(count.values())}")
    print(f"Part 2: {sum(count.values())}")

if __name__ == "__main__":
    main()
