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

def is_true(current: int, target: int, operands: Operands, index: int) -> bool:
    '''
    - No precedence
    - Evaluate calc left to right
    - Only `+` and `*` operators available

    Fill every operand with every operator combination possible,
    then check the result of every combination against our target equation result

    Returns ->
    - True if at least one combination is correct
    - False otherwise
    '''
    if index == len(operands):
        return current == target
    return  is_true(current * operands[index], target, operands, index + 1) or \
            is_true(current + operands[index], target, operands, index + 1)

def is_true_third_operator(current: int, target: int, operands: Operands, index: int) -> bool:
    '''
    - No precedence
    - Evaluate calc left to right
    - Only `+`, `*` and `||` operators available
    - `||` is a concatenation operator, E.G.:
    ```
    >>> 2 || 35 -> 235
    ```

    Fill every operand with every operator combination possible,
    then check the result of every combination against our target equation result

    Returns ->
    - True if at least one combination is correct
    - False otherwise
    '''
    if index == len(operands):
        return current == target
    return  is_true_third_operator(concat(current, operands[index]), target, operands, index + 1) or \
            is_true_third_operator(current * operands[index], target, operands, index + 1) or \
            is_true_third_operator(current + operands[index], target, operands, index + 1)

def sum_true_equations(equations: Equations, equation_verification: Verif_function) -> int:
    '''
    Check if each equation is possible and sum their results
    '''
    sum: int = 0
    for results, operands in equations:
        if equation_verification(operands[0], results, operands, 1):
            sum += results
    return sum

def main() -> None:
    equations: Equations = load_equations()
    print(f"Part1: {sum_true_equations(equations, equation_verification=is_true)}")
    print(f"Part2: {sum_true_equations(equations, equation_verification=is_true_third_operator)}")

if __name__ == '__main__':
    main()
