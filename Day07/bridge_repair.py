# Semantics
from collections.abc import Callable

type Operand = int
type Operands = list[Operand]
type Result = int

# Types
type Equation = tuple[Result, Operands]
type Equations = list[Equation]
type Verif_function = Callable[[int, int, Operands, int], int]

def load_equations() -> Equations:
    '''
    Read our input file for the day
    Parse it to have a list of `Equation` -> (`tuple[Result, Operands]`)

    Line format =>
    `eq_res: *numbers`
    '''
    with open('input.txt') as f:
        input = f.read()

    equations: Equations = [
        (
            int(res_s),
            [int(operand) for operand in op_s.strip().split(' ')]
        )
        for line in input.strip().split('\n')
        for res_s, op_s in [line.split(':')]
    ]

    return equations

def concat(first: int, second: int) -> int:
    '''
    - `||` is a concatenation operator, E.G.:
    ```
    >>> 2 || 35 -> 235
    ```
    '''
    return(int(str(first) + str(second)))

def is_true_combined(current: int, target: int, operands: Operands, index: int, use_concat: bool = False) -> bool:
    '''
    - No precedence
    - Evaluate calc left to right
    - Operators available: `+`, `*`, and optionally `||` (concatenation)

    If use_concat is True, we will include the concatenation operator `||`
    which joins the current value and the operand as a string, then converts it back to an integer.

    Returns ->
    - True if at least one combination is correct
    - False otherwise
    '''
    if index == len(operands):
        return current == target

    if use_concat:
        return (
            is_true_combined(concat(current, operands[index]), target, operands, index + 1, use_concat) or \
            is_true_combined(current * operands[index], target, operands, index + 1, use_concat) or
            is_true_combined(current + operands[index], target, operands, index + 1, use_concat)
        )
    else:
        return (
            is_true_combined(current * operands[index], target, operands, index + 1, use_concat) or \
            is_true_combined(current + operands[index], target, operands, index + 1, use_concat)
        )

def sum_true_equations(equations: Equations, use_concat: bool) -> int:
    '''
    Check if each equation is possible and sum their results
    '''
    sum: int = 0
    for results, operands in equations:
        if is_true_combined(operands[0], results, operands, 1, use_concat):
            sum += results
    return sum

def main() -> None:
    equations: Equations = load_equations()
    print(f"Part1: {sum_true_equations(equations, use_concat=False)}")
    print(f"Part2: {sum_true_equations(equations, use_concat=True)}")

if __name__ == '__main__':
    main()
