# Semantics
type Operand = int
type Operands = list[Operand]
type Result = int

type Equation = tuple[Result, Operands]
type Equations = list[Equation]

def load_equations() -> Equations:
    with open('input.txt') as f:
        input = f.read()

    # Line -> eq_res: *numbers
    test = "190: 10 19\n3267: 81 40 27\n83: 17 5\n156: 15 6\n7290: 6 8 6 15\n161011: 16 10 13\n192: 17 8 14\n21037: 9 7 18 13\n292: 11 6 16 20"

    equations: Equations = [
        (
            int(res_s),
            [int(operand) for operand in op_s.strip().split(' ')]
        )
        for line in test.strip().split('\n')
        for res_s, op_s in [line.split(':')]
    ]

    return equations


def main() -> None:
# Possible operators + *
# Find operators such that Result is true
# No precedence, always evaluate calculation left to right
    equations: Equations = load_equations()
    print(f"equations -> {equations}")

if __name__ == '__main__':
    main()
