
import tkinter as tk

class mainGUI:
    """
    GUI for the Minesweeper game.
    """

    def __init__(self, master, boardmaker):
        """
        Initializes the main GUI.

        Args:
            master (tk.Tk): The main application window.
            boardmaker (mineboard): The Minesweeper board object.
        """
        self.master = master
        master.title("Minesweeper")
        self.board = boardmaker.mineField
        self.cols = boardmaker.cols
        self.rows = boardmaker.rows
        self.buttons = []
        self.gameOver = False

        self.makeWidgets()
        self.calculateAdjBombs()

    def makeWidgets(self):
        """
        Creates the grid of buttons for the game.
        """
        for row in range(self.rows):
            button_row = []
            for col in range(self.cols):
                button = tk.Button(
                    self.master,
                    width=2,
                    height=1,
                    command=lambda r=row, c=col: self.showCell(r, c)
                )
                button.grid(row=row, column=col)
                button.bind("<Button-3>", lambda event, r=row, c=col: self.placeFlag(r, c))
                button_row.append(button)
            self.buttons.append(button_row)

    def calculateAdjBombs(self):
        """
        Calculates the number of adjacent bombs for each cell.
        """
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 'bomb':
                    adjBombs = self.countAdjBombs(i, j)
                    self.board[i][j] = adjBombs

    def countAdjBombs(self, row, col):
        """
        Counts the number of bombs adjacent to a given cell.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        Returns:
            int: The number of adjacent bombs.
        """
        count = 0
        for r in range(max(0, row - 1), min(self.rows, row + 2)):
            for c in range(max(0, col - 1), min(self.cols, col + 2)):
                if self.board[r][c] == 'bomb':
                    count += 1
        return count

    def showCell(self, row, col):
        """
        Reveals a cell on the board.

        Args:
            row (int): The row index of the cell to reveal.
            col (int): The column index of the cell to reveal.
        """
        if self.gameOver or self.buttons[row][col]['state'] == 'disabled':
            return
        if self.board[row][col] == 'bomb':
            self.gameOver = True
            self.showAllBombs()
            self.gameOverPrompt()
        else:
            self.showEmpties(row, col)
    def gameOverPrompt(self):
        """
        Displays a game over message with an option to restart.
        """
        game_over_window = tk.Toplevel(self.master)
        game_over_window.title("Game Over")

        window_width = 250
        window_height = 100
        screen_width = game_over_window.winfo_screenwidth()
        screen_height = game_over_window.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        game_over_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        tk.Label(game_over_window, text="You hit a bomb! Game Over.", font=("Arial", 12)).pack(pady=10)

        def restart_game():
            """
            Handles the restart button click.
            """
            game_over_window.destroy()
            # Only restart if a callback is set
            if self.restart_callback:
                self.restart_callback()

        tk.Button(game_over_window, text="Restart", command=restart_game, width=10).pack(pady=5)

        game_over_window.grab_set()  # Make the game over window modal (block interaction with other windows)
        
    def set_restart_callback(self, callback):
        """
        Sets the callback function to be called when the game needs to be restarted.
        """
        self.restart_callback = callback

    def showEmpties(self, row, col):
        """
        Reveals empty cells recursively.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
        """
        if self.buttons[row][col]['state'] == 'disabled':
            return

        if self.board[row][col] == 0:
            self.buttons[row][col]["text"] = ""
            self.buttons[row][col]["state"] = "disabled"
        else:
            self.buttons[row][col]["text"] = str(self.board[row][col])
            self.buttons[row][col]["state"] = "disabled"

        if self.board[row][col] == 0:
            for r in range(max(0, row - 1), min(self.rows, row + 2)):
                for c in range(max(0, col - 1), min(self.cols, col + 2)):
                    if (r != row or c != col) and self.board[r][c] != "bomb":
                        self.showEmpties(r, c)

    def placeFlag(self, row, col):
        """
        Places or removes a flag on a cell.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
        """
        if self.gameOver:
            return
        button = self.buttons[row][col]
        if button["state"] != "disabled":
            if button["text"] == "":
                button["text"] = "F"
            elif button["text"] == "F":
                button["text"] = ""

    def showAllBombs(self):
        """
        Reveals all bombs on the board.
        """
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == 'bomb':
                    self.buttons[row][col]["text"] = 'B'

