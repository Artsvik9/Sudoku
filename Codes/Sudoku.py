import random
import time
from collections import deque
import math
import pandas as pd


# Helper functions
def is_valid(board, row, col, num, grid_size, subgrid_size):
    """Check if placing num in board[row][col] is valid."""
    for i in range(grid_size):
        if board[row][i] == num or board[i][col] == num:
            return False
        subgrid_row = subgrid_size * (row // subgrid_size)
        subgrid_col = subgrid_size * (col // subgrid_size)
        if board[subgrid_row + i // subgrid_size][subgrid_col + i % subgrid_size] == num:
            return False
    return True


def find_empty_cell(board, grid_size):
    """Find the first empty cell in the grid."""
    for row in range(grid_size):
        for col in range(grid_size):
            if board[row][col] == 0:
                return row, col
    return None


# Solvers
def solve_sudoku_bfs(board, grid_size, subgrid_size):
    """Solve Sudoku using Breadth-First Search."""
    queue = deque([board])
    while queue:
        current_board = queue.popleft()
        empty_cell = find_empty_cell(current_board, grid_size)
        if not empty_cell:
            return current_board  # Solved
        row, col = empty_cell
        for num in range(1, grid_size + 1):
            if is_valid(current_board, row, col, num, grid_size, subgrid_size):
                new_board = [r[:] for r in current_board]
                new_board[row][col] = num
                queue.append(new_board)
    return None


def solve_sudoku_dfs(board, grid_size, subgrid_size):
    """Solve Sudoku using Depth-First Search."""
    stack = [board]
    while stack:
        current_board = stack.pop()
        empty_cell = find_empty_cell(current_board, grid_size)
        if not empty_cell:
            return current_board  # Solved
        row, col = empty_cell
        for num in range(1, grid_size + 1):
            if is_valid(current_board, row, col, num, grid_size, subgrid_size):
                new_board = [r[:] for r in current_board]
                new_board[row][col] = num
                stack.append(new_board)
    return None


def solve_sudoku_ids(board, grid_size, subgrid_size):
    """Solve Sudoku using Iterative Deepening Search."""
    def dfs_limited(board, depth):
        empty_cell = find_empty_cell(board, grid_size)
        if not empty_cell:
            return board  # Solved
        if depth == 0:
            return None
        row, col = empty_cell
        for num in range(1, grid_size + 1):
            if is_valid(board, row, col, num, grid_size, subgrid_size):
                new_board = [r[:] for r in board]
                new_board[row][col] = num
                result = dfs_limited(new_board, depth - 1)
                if result:
                    return result
        return None

    for depth in range(1, grid_size ** 2 + 1):
        result = dfs_limited(board, depth)
        if result:
            return result
    return None


# Generate Sudoku
def generate_sudoku(grid_size):
    subgrid_size = int(math.sqrt(grid_size))
    solved_board = [[((i * subgrid_size + i // subgrid_size + j) % grid_size) + 1 for j in range(grid_size)]
                    for i in range(grid_size)]
    for i in range(0, grid_size, subgrid_size):
        rows = list(range(i, i + subgrid_size))
        cols = list(range(i, i + subgrid_size))
        random.shuffle(rows)
        random.shuffle(cols)
        solved_board[i:i + subgrid_size] = [solved_board[r] for r in rows]
        for row in solved_board:
            row[i:i + subgrid_size] = [row[c] for c in cols]
    return solved_board


def remove_numbers(board, difficulty, grid_size):
    empty_cells = {"easy": grid_size ** 2 // 4, "medium": grid_size ** 2 // 2, "hard": 3 * grid_size ** 2 // 4}[difficulty]
    for _ in range(empty_cells):
        row, col = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
        board[row][col] = 0
    return board


# Solve with models and format results
def solve_with_models(board, grid_size, subgrid_size, models):
    results = []
    for model_name, model_function in models.items():
        start_time = time.time()
        solution = model_function(board, grid_size, subgrid_size)
        end_time = time.time()
        solved = solution is not None
        results.append({
            "Grid Size": grid_size,
            "Heuristic": model_name,
            "Difficulty": difficulty,
            "Time Taken (s)": round(end_time - start_time, 4),
            "Solved": solved
        })
    return pd.DataFrame(results)


# Main
if __name__ == "__main__":
    grid_size = 9
    difficulty = "medium"
    subgrid_size = int(math.sqrt(grid_size))

    # Generate Sudoku
    sudoku_grid = generate_sudoku(grid_size)
    sudoku_grid = remove_numbers(sudoku_grid, difficulty, grid_size)

    print("Original Sudoku Grid:")
    for row in sudoku_grid:
        print(" ".join(str(cell) if cell != 0 else "." for cell in row))

    # Specify solving models
    models = {
        "BFS": solve_sudoku_bfs,
        "DFS": solve_sudoku_dfs,
        "IDS": solve_sudoku_ids
    }

    # Solve and display results
    results = solve_with_models(sudoku_grid, grid_size, subgrid_size, models)
    print("\nResults:")
    print(results)



