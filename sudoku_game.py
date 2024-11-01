import tkinter as tk
from tkinter import messagebox
import random

# Initialize the board
def initialize_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    fill_board(board)
    return create_puzzle(board)

# Fill the board with a valid Sudoku solution (using backtracking)
def fill_board(board):
    empty_spot = find_empty(board)
    if not empty_spot:
        return True
    row, col = empty_spot
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if fill_board(board):
                return True
            board[row][col] = 0
    return False

# Remove numbers from the board to create a Sudoku puzzle
def create_puzzle(board, attempts=30):
    while attempts > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        backup = board[row][col]
        board[row][col] = 0
        copy_board = [row[:] for row in board]
        if not fill_board(copy_board):
            board[row][col] = backup
        else:
            attempts -= 1
    return board

# Check if a number is valid in a given position
def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(9)]:
        return False
    box_x, box_y = row // 3 * 3, col // 3 * 3
    for i in range(box_x, box_x + 3):
        for j in range(box_y, box_y + 3):
            if board[i][j] == num:
                return False
    return True

# Find an empty position on the board
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

# Check if the current board is complete and correct
def check_complete():
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return False
            if not is_valid(puzzle, i, j, puzzle[i][j]):
                return False
    return True

# Initialize the GUI
root = tk.Tk()
root.title("Sudoku")

# Initialize the puzzle
puzzle = initialize_board()
entries = []

# Populate the board with Tkinter Entry widgets
for i in range(9):
    row_entries = []
    for j in range(9):
        entry = tk.Entry(root, width=3, font=("Arial", 16), justify="center")
        entry.grid(row=i, column=j, padx=5, pady=5)
        if puzzle[i][j] != 0:
            entry.insert(0, str(puzzle[i][j]))
            entry.config(state="disabled")  # Disable pre-filled cells
        row_entries.append(entry)
    entries.append(row_entries)

# Function to update puzzle based on user input
def update_puzzle():
    for i in range(9):
        for j in range(9):
            value = entries[i][j].get()
            if value.isdigit() and 1 <= int(value) <= 9:
                puzzle[i][j] = int(value)
            else:
                puzzle[i][j] = 0

# Check solution when "Check" button is pressed
def check_solution():
    update_puzzle()
    if check_complete():
        messagebox.showinfo("Sudoku", "Congratulations! You've completed the puzzle correctly.")
    else:
        messagebox.showerror("Sudoku", "The puzzle is not yet correct. Keep trying!")

# Add a button to check the solution
check_button = tk.Button(root, text="Check Solution", command=check_solution)
check_button.grid(row=9, column=4, pady=10)

# Run the main loop
root.mainloop()
