This project implements a Sudoku solver using Constraint Satisfaction Problem (CSP) techniques. It evaluates algorithms such as backtracking, forward checking, and heuristics like Minimum Remaining Value (MRV), Least Constraining Value (LCV), and the AC-3 algorithm. The solver is designed to handle puzzles of varying difficulty levels and provides insights into the performance of different solving techniques.

Features

CSP Algorithms: Implements backtracking, AC-3, and forward checking.
Heuristics: Optimizes solving using MRV, LCV, and degree heuristics.
Performance Metrics: Tracks time complexity and steps for solving puzzles.
Versatility: Handles easy, medium, and hard Sudoku puzzles.
Requirements

To run the program, ensure the following are installed:

Python 3.8 or later
Libraries:
pandas
Standard Python libraries (math, random, collections, time)
Install missing libraries using:

pip install pandas

Usage

1. Clone or download the repository:

git clone https://github.com/your-repo/sudoku-solver.git
cd sudoku-solver

2. Run the Sudoku.py script:

python Sudoku.py

3. Input a Sudoku puzzle or use a pre-loaded example.

Input Format
The program accepts puzzles as a 2D list where 0 represents empty cells. Example:

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    ...
]


Output

* Solved Sudoku puzzle
* Performance statistics:
	** Time complexity
	** Number of steps
	
File Structure

Sudoku.py: Main script containing the solver logic.
README.md: Project documentation.
