Doing the Advent Of Code 2024

First 3 day are done in C# for language specific learning purposes, the remaining days are in Python

Interesting notes about learning points / challenge / thoughts about each days:

- Day01 => Implementing an indexer and a custom `defaultDict` in C#, quite the learning experience
- Day02 => Clean and easy to code solution, but there is an optimal O(N) to do here
- Day03 => Regex in C#
- Day04 => Numpy Array matrixes diagonals manipulation. Unpacking to zip for vertical observation
- D04p2 => Using ASCII values to ignore directions
- Day05 => Use of a HashMap for every rule, keeping an update slice of prev-next of our current update: allow to never check the rules in more than one direction
- Day06 => In first iteration rotated the whole map instead of the guard, changed it to fit part 2
- D06p2 => Lots of time optimisation possible, the best i found was checking for loops only for part1 elems, and triggering it as soon as we visited a same place with a same direction, lots of set usage for O(1) insertion
- Day07 => Dict and tuple comprehension order in python is non intuitive
