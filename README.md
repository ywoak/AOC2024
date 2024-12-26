Doing the Advent Of Code 2024

First 3 day are done in C# to learn the language
The remaining days are in Python to improve my skills

Interesting notes about learning points / challenge / thoughts about each days:

- Day01 => Implementing an indexer and a custom `defaultDict` in C#
- Day02 => Clean and easy to code solution, but time complexity is not optimal
- Day03 => Regex in C#
- Day04 => Array matrixes diagonals manipulation black magic
- D04p2 => Using ASCII values to ignore directions
- Day05 => Use of a HashMap for every rule, keeping an update slice of prev-next of our current update: allow to never check the rules in more than one direction
- Day06 => In my first iteration I rotated the whole map instead of the guard, GoogleMap style
- D06p2 => Time optimisation -> checking for loops only for part1 elems | triggering loop if we visited same place at same direction
- Day07 => Comprehensions order in python are not intuitive
- Day08 => Some interesting recursivity
- Day09 => My first sliding windows algorithm ! :)
- Day10 => My first graph traversal algorithm ! :)
- Day11 => Used a cache at first, but having a solution without printing at all instead is done in 0.01s
- Day12 => My best code until now, nice and simple solution to know how many side a shape has in part2, an overall really fast solution (0.1s on input without Pypy)
- Day13 => The list comprehension and generator expression used for parsing the input is clean ! Starting to love this feature the most out of python
- D13p2 => Required mathematical help from friend, and Rational from sympy to avoid approximating rational numbers
- Day14 => Nothing particularly interesting nor challenging today, straight forward programming, the parsing comprehension was nice and reading was done with `open(0)` to use with Utils/aoc.py
- Day15 => IRL is taking some times, in the interest of time i will probably finish this challenge with part 1 only for now, and revisit part 2 for day 15-25 later
- Day16 => Getting all possible way to the end, reconstructing each path and then checking the highest score, works well for test input but a bit too slow for real input, a djikstra would probably be better
- Day17 => Modulo 8 is equivalent to & 7 (b111), we keep only the last 3 bit
