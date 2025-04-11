from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Validate rows
        for row in range(len(board)):
            digitSet = set()
            for col in range(len(board)):
                if board[row][col] != ".":
                    if board[row][col] in digitSet:
                        return False
                    digitSet.add(board[row][col])

        # Validate columns
        for col in range(len(board)):
            digitSet = set()
            for row in range(len(board)):
                if board[row][col] != ".":
                    if board[row][col] in digitSet:
                        return False
                    digitSet.add(board[row][col])

        # Validate squares
        for row in range(1, len(board), 3):
            for col in range(1, len(board), 3):
                digitSet = set()
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if board[row + i][col + j] != ".":
                            if board[row + i][col + j] in digitSet:
                                return False
                            digitSet.add(board[row + i][col + j])

        return True


def main():
    s = Solution()
    print(
        s.isValidSudoku(
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
    )
    print(
        s.isValidSudoku(
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
    )
    print(
        s.isValidSudoku(
            [
                [".", ".", ".", ".", "5", ".", ".", "1", "."],
                [".", "4", ".", "3", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", "3", ".", ".", "1"],
                ["8", ".", ".", ".", ".", ".", ".", "2", "."],
                [".", ".", "2", ".", "7", ".", ".", ".", "."],
                [".", "1", "5", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", "2", ".", ".", "."],
                [".", "2", ".", "9", ".", ".", ".", ".", "."],
                [".", ".", "4", ".", ".", ".", ".", ".", "."],
            ]
        )
    )


if __name__ == "__main__":
    main()
