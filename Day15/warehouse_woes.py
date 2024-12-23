def parse_input() -> tuple[list[list[str]], str]:
    input: list[str] = open(0).read().strip().split('\n\n')
    map: list[list[str]] = [[char for char in line] for line in input[0].split('\n')]
    commands: str = input[1].replace("\n", "")

    return map, commands

def main():
    map, commands = parse_input()

    print(map, end="\n\n")
    print(commands)

if __name__ == "__main__":
    main()
