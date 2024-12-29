import random

class mineboard:
    bombCount = 0
    
    def __init__(self,difficulty = 'Easy'):
        self.difficulty = difficulty
        self.mineField = self.initMinefield(self.difficulty)

    def initMinefield(self,diff):
        self.mineField = []
        match (diff):
            case 'Easy':
                self.bombCount = 10
                rows = 9
                cols = 9
            case 'Medium':
                self.bombCount = 40
                rows = 16
                cols = 16
            case 'Hard':
                self.bombCount = 99
                rows = 30
                cols = 16
        for i in range(rows):
            temp = []
            for j in range(cols):
                temp.append(0)
            self.mineField.append(temp)
        self.populateMinefield(rows, cols,self.bombCount)
        return self.mineField
    
    def populateMinefield(self,rows, cols,bombcount):
        bombs = 0
        while bombs < bombcount:
            row_index = random.randint(0, rows - 1)
            col_index = random.randint(0, cols - 1)

            if self.mineField[row_index][col_index] == 0:
                self.mineField[row_index][col_index] = 'bomb'
                bombs += 1
        return self.mineField
