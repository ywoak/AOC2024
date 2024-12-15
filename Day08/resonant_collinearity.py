type Map = list[list[str]]

def load_map() -> Map:
    map: Map = []

    with open('test.txt') as f:
        input = f.read()
    for line in input.split('\n'):
        if bool(line):
            map.append(list(line))
    return map

def main() -> None:
    map: Map = load_map()
    for r in map: print(r)

if __name__ == '__main__':
    main()
