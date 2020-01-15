class Solution:
    def isValidSudoku(self, board):
        if not board:
            return False
        for col in range(len(board)):
            vectorRow = 0
            vectorCol = 0
            for row in range(len(board[col])):
                currentRowWiseNumber = board[col][row]
                currentColWiseNumber = board[row][col]
                # print(col, row, currentRowWiseNumber, currentColWiseNumber)
                if currentRowWiseNumber.isdigit():
                    currentRowWiseNumber = int(currentRowWiseNumber)
                    vectorRow = self.updateVector(vectorRow, currentRowWiseNumber)
                    if not vectorRow:
                        # print("False at Row: ", col, row)
                        return False
                if currentColWiseNumber.isdigit():
                    currentColWiseNumber = int(currentColWiseNumber)
                    vectorCol = self.updateVector(vectorCol, currentColWiseNumber)
                    if not vectorCol:
                        # print("False at Col: ", col, row)
                        return False
        for subSudokuCol in range(3, 10, 3):
            for subSudokuRow in range(3, 10, 3):
                vector = 0
                for col in range(subSudokuCol - 3, subSudokuCol):
                    for row in range(subSudokuRow - 3, subSudokuRow):
                        number = board[col][row]
                        if number.isdigit():
                            # print(number)
                            number = int(number)
                            vector = self.updateVector(vector, number)
                            if not vector:
                                # print(
                                #     "False at Row: ",
                                #     subSudokuCol,
                                #     subSudokuRow,
                                #     col,
                                #     row,
                                # )
                                return False
        return True

    def updateVector(self, vector, number):
        bit = 1 << (number - 1)
        if vector & bit == 0:
            vector = vector ^ bit
            return vector
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    arr = {
        "RightSolution": [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ],
        "WrongRow": [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", "3", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ],
        "WrongColumn": [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", "9", ".", ".", "8", ".", ".", "7", "4"],
        ],
        "WrongSubBox": [
            ["5", "3", "9", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ],
    }
    print(s.isValidSudoku(arr["RightSolution"]))
    print(s.isValidSudoku(arr["WrongRow"]))
    print(s.isValidSudoku(arr["WrongColumn"]))
    print(s.isValidSudoku(arr["WrongSubBox"]))
