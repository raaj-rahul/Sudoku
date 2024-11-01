# Sudoku Game in Python

This is a graphical Sudoku game built using Python and Tkinter. The game generates a random Sudoku puzzle that players can solve by filling in the empty cells.

## Game Overview

- **GUI-based**: Built with Tkinter, this game provides a visual interface for players.
- **Puzzle Generation**: Each game generates a new puzzle with a unique solution.
- **Solution Checking**: A button allows players to check if their solution is correct.

## Features

- **9x9 Grid**: The board has a 9x9 layout, split into 3x3 subgrids.
- **Interactive Cells**: Players can enter values in empty cells to complete the puzzle.
- **Check Solution**: The game verifies if the board is filled correctly and displays a success or error message.

## Getting Started

### Prerequisites

- **Python 3.x**: Ensure Python is installed. You can download it from [python.org](https://www.python.org/downloads/).
- **Tkinter**: Tkinter typically comes with Python, but you can verify by running `python -m tkinter` in a command prompt.

### Installation

1. **Download or Clone** this repository.
2. Save the code as `sudoku_game.py` in your desired folder.

### Running the Game

1. Open a command prompt or terminal.
2. Navigate to the folder where `sudoku_game.py` is saved.
3. Run the following command:

   ```bash
   python sudoku_game.py
   ```

   This command will open the Sudoku game window.

## Instructions for Playing

1. A 9x9 Sudoku board will appear, with some cells pre-filled.
2. To solve the puzzle, click on an empty cell and enter a number between 1 and 9.
3. Once you’ve completed the puzzle, click the **Check Solution** button.
4. If the puzzle is correctly solved, you’ll see a success message. If not, an error message will appear.

## Code Structure

- **initialize_board()**: Generates a Sudoku puzzle with a unique solution.
- **fill_board()**: Fills a board completely as a valid Sudoku solution using backtracking.
- **create_puzzle()**: Removes numbers from the completed board to create the puzzle.
- **is_valid()**: Checks if a number is valid in a given position.
- **find_empty()**: Finds the next empty cell on the board.
- **update_puzzle()**: Updates the puzzle based on user input.
- **check_complete()**: Checks if the user has completed the puzzle correctly.


## Contributing

Feel free to submit pull requests or suggest improvements. This project is open for contributions to enhance functionality, such as adding hints or error highlighting.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This project uses the Tkinter library for the graphical user interface.
