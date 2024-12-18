from collections import defaultdict

type Stone = str
type Stones = list[Stone]

type Count = defaultdict[Stone, int]

def load_map():
    with open('input.txt') as f:
        input = f.read()
    return [c for c in input.split(' ')]

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

        for e in tmp:
            cpy[e] += val
    return cpy

def fill_cache(stones: Stones, count_cache: Count) -> Count:
    for stone in stones:
        count_cache[stone] += 1
    return count_cache

def main():
    stones: Stones = load_map()
    count_cache: Count = defaultdict(int)
    count_cache = fill_cache(stones, count_cache)
    for _ in range(25):
        count_cache = blink(count_cache)

    print(f"Part 1: {sum(count_cache.values())}")

if __name__ == "__main__":
    main()
