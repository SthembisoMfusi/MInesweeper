import random

class mineboard:
    """
    Represents a Minesweeper board.
    """

    def __init__(self, difficulty='Easy'):
        """
        Initializes the Minesweeper board with the given difficulty.

        Args:
            difficulty (str): The difficulty level ('Easy', 'Medium', or 'Hard').
        """
        self.difficulty = difficulty
        self.bombCount = 0
        self.rows = 0
        self.cols = 0
        self.mineField = []
        self.initMinefield(self.difficulty)

    def initMinefield(self, diff):
        """
        Initializes the minefield grid based on the difficulty.

        Args:
            diff (str): The difficulty level.
        """
        if diff == 'Easy':
            self.bombCount = 10
            self.rows = 9
            self.cols = 9
        elif diff == 'Medium':
            self.bombCount = 40
            self.rows = 16
            self.cols = 16
        elif diff == 'Hard':
            self.bombCount = 99
            self.rows = 30
            self.cols = 16
        else:
            raise ValueError("Invalid difficulty level")

        for i in range(self.rows):
            temp = []
            for j in range(self.cols):
                temp.append(0)
            self.mineField.append(temp)
        self.populateMinefield(self.rows, self.cols, self.bombCount)
        return self.mineField

    def populateMinefield(self, rows, cols, bombcount):
        """
        Randomly places bombs on the minefield.

        Args:
            rows (int): The number of rows in the minefield.
            cols (int): The number of columns in the minefield.
            bombcount (int): The number of bombs to place.
        """
        bombs = 0
        while bombs < bombcount:
            row_index = random.randint(0, rows - 1)
            col_index = random.randint(0, cols - 1)

            if self.mineField[row_index][col_index] == 0:
                self.mineField[row_index][col_index] = 'bomb'
                bombs += 1
        return self.mineField
