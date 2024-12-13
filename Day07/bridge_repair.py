# Semantics
type Operand = int
type Operands = list[Operand]
type Result = int

# Types
type Equation = tuple[Result, Operands]
type Equations = list[Equation]

def load_equations() -> Equations:
    '''
    Read our input file for the day
    Parse it to have a list of `Equation` -> (`tuple[Result, Operands]`)

    Line format =>
    `eq_res: *numbers`
    '''
    with open('input.txt') as f:
        input = f.read()

    #test = "190: 10 19\n3267: 81 40 27\n83: 17 5\n156: 15 6\n7290: 6 8 6 15\n161011: 16 10 13\n192: 17 8 14\n21037: 9 7 18 13\n292: 11 6 16 20"

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
    return  is_true(current * operands[index], target, operands, index + 1) or \
            is_true(current + operands[index], target, operands, index + 1) or \
            is_true(concat(current, operands[index]), target, operands, index + 1)

def sum_true_equations(equations: Equations) -> int:
    '''
    Check if each equation is possible and sum there results
    '''
    sum: int = 0
    for results, operands in equations:
        if is_true(operands[0], results, operands, 1):
            sum += results
    return sum

def sum_true_equations_third_operator(equations: Equations) -> int:
    '''
    Check if each equation is possible and sum there results
    We use this one for part 2
    '''
    sum: int = 0
    for results, operands in equations:
        if is_true_third_operator(operands[0], results, operands, 1):
            sum += results
    return sum

def main() -> None:
    equations: Equations = load_equations()
    print(f"Part1: {sum_true_equations(equations)}")
    print(f"Part2: {sum_true_equations_third_operator(equations)}")

if __name__ == '__main__':
    main()
