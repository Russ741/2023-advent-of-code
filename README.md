# Advent of Code 2023

(Almost) all of my solutions to the [2023 edition](https://adventofcode.com/2023) of [Advent of Code](https://adventofcode.com/2023/about).

## Summary

Advent of Code is a series of Christmas-themed programming challenges from Dec. 1st-25th:
* At midnight (Eastern), one problem description (in narrative prose), sample input/answer, and input file are posted.
  * Input files are personalized/randomized for each contestant.
* The contestant submits the answer (usually a 64-bit or less integer) for the given problem and input.
* When the contestant submits the correct answer, the second challenge's problem description is unlocked.
  * The second challenge usually uses the same input file as the first, but the problem requires interpreting it in a more computationally intensive way.
* The contestant submits the answer (same format) for the second problem.

My solutions are organized by day, with independent Python files for part 1 and part 2.

## Tool-Assisted Solves

In Advent of Code, the contestant only needs to come up with a solution for a single specific, known input, and they do not need to "show their work". <br />
Contrast with LeetCode, etc. where the candidate must provide a self-contained piece of code with limited dependencies that produces the right answers for a test suite of opaque inputs spanning the problem space. <br />
Advent of Code inputs are also sometimes structured to yield an answer more readily than the general formulation presented in the problem. <br />
As such, it lends itself to tool-assisted (semi-automated) solves.

Specific examples:
* [Day 21 Part 2](https://github.com/Russ741/2023-advent-of-code/blob/main/21/02.py): This was an involved Python -> Google Sheets -> Python process (detailed [here](https://github.com/Russ741/2023-advent-of-code/blob/main/21/README.md)).
  * The formula derived by polynomial regression could also be found by summing contributions from core (completely reachable) and edge (partially reachable) grid tiles - no Google Sheets required.
  * Thoughts about a potential fully-generalizable solution are in the [writeup](https://github.com/Russ741/2023-advent-of-code/blob/main/21/README.md).
* [Day 24 Part 2](https://github.com/Russ741/2023-advent-of-code/blob/main/24/02-sympy.py): I used sympy to solve a system of equations for a few hailstones.
  * There's presumably an algebraic approach to combining the hailstones' paths without using this library.
* [Day 25 part 1](https://github.com/Russ741/2023-advent-of-code/blob/main/25/01.py): I found the three edges to cut by [graphing it in graphviz](https://github.com/Russ741/2023-advent-of-code/blob/main/25/output.svg) and manual inspection.
  * A fully automatic algorithmic approach would probably resemble max-flow/min-cut.
