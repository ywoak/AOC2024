# Program list of number
# Three register A B C
#
# Eight instructions identified by opcode
# take next number as input for operand
#
# Instruction pointer start at 0
# Identify position in the program from which the next opcode will be read
# Step by 2 every time to move past instruction opcode and operand
#
# Each instruction specify type of its operand
# Literal operand value is operand itself
# Combo operands 0 through 3 represent literal values 0 through 3
# Combo operand 4 represents the value of register A
# Combo operand 5 represents the value of register B
# Combo operand 6 represents the value of register C
# Combo operand 7 is reserved and will not appear in valid programs
#
# Instructions
# adv 0 performs division. The numerator is the value in the A register. The denominator is found by raising 2 to the power of the instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then written to the A register.
# bxl 1 calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.
# bst 2 calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.
# jnz 3 does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
# bxc 4 calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)
# out 5 calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)
# bdv 6 works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)
# cdv 7 works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)

import re

def load_map():
    registers, program = open(0).read().strip().split('\n\n')
    A, B, C = [int(reg) for reg in registers.split('\n')]
    program = program.split(',')

    print(f"registers is\n{registers}\nprogram is\n{program}")
    return A, B, C, program

def main():
    A, B, C, program = load_map()

if __name__ == "__main__":
    main()
