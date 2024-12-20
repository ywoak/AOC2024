import sys

# Charge l'entrée depuis stdin
input = sys.stdin.read()

def load_input() -> str:
    """
    Load stdin
    """
    return input.strip()

def load_lines() -> list[str]:
    """
    Load a list of line from stdin
    """
    return [line for line in input.strip().split('\n')]

def load_int() -> list[list[int]]:
    """
    Load a list of list of int for every line for every elem separated by whitespace
    """
    return [[int(elem)] for line in input.strip().split('\n') for elem in line.split(' ')]

def load_str() -> list[list[str]]:
    """
    Load a list of list of char for every char in every line
    """
    return [[char] for line in input.strip().split('\n') for char in line]
