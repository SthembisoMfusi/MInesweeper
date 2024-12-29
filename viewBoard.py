
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
            tk.messagebox.showinfo('Game Over', 'You hit a bomb')
        else:
            self.showEmpties(row, col)

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

