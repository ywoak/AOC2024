def load_map() -> tuple[int, int, int, list[int]]:
    registers, program = open(0).read().strip().split('\n\n')

    A, B, C = [int(reg) for reg in registers.split('\n')]
    program = [int(inst) for inst in program.split(',')]

    return A, B, C, program

def combo(operand: int, A: int, B: int, C: int) -> int:
    if operand < 4:
        return operand
    match operand:
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C
    return -1

def main():
    A, B, C, program = load_map()
    ip = 0
    output = ""
    while ip < len(program) - 1:
        opcode = int(program[ip])
        operand = int(program[ip + 1])

        match opcode:
            case 0:
                A = A // (2 ** combo(operand, A, B, C)) # // To truncate to int
            case 1:
                B = B ^ operand
            case 2:
                B = combo(operand, A, B, C) & 7 # (% 8 == & 7)
            case 3:
                if (A != 0):
                    ip = operand
                    continue # With a jump operation, avoid the usual iteration
            case 4:
                B = B ^ C
            case 5:
                output += str(combo(operand, A, B, C) & 7) + ','
            case 6:
                B = A // (2 ** combo(operand, A, B, C))
            case 7:
                C = A // (2 ** combo(operand, A, B, C))

        ip += 2
    print(f"Part 1: {output[:-1]}") # Remove last commas

if __name__ == "__main__":
    main()
