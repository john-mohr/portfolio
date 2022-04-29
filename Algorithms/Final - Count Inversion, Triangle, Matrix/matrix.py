"""
    matrix.py
    Implementation of a dynamic programming algorithm to
    find the smallest sum of m adjacent numbers in
    an m x n matrix (m rows, n columns)

    [John David Mohr]
"""

def matrix(board): 
    # your code goes here:
    print(len(board), len(board[0]))
    resultBoard = board
    for i in range(1, len(board)):
        sum = 100000
        for j in range(len(board[0])):
            if j > 0 and j < len(board[0]) - 1:
                resultBoard[i][j] += min(board[i - 1][j], board[i - 1][j - 1], board[i - 1][j + 1])

            elif j > 0:
                resultBoard[i][j] += min(board[i - 1][j], board[i - 1][j - 1])

            elif (j < len(board[0]) - 1):
                resultBoard[i][j] += min(board[i - 1][j], board[i - 1][j + 1])

            if board[i][j] < sum:
                sum = resultBoard[i][j]

    return sum




if __name__ == "__main__":
    board = [[1,2,3],[4,5,6],[7,0,2]]

    print(matrix(board))

