"""
    triangle.py
    Implementation of a dynamic programming algorithm to
    find the smallest sum of m adjacent numbers in
    an m-row triangle

    [John David Mohr]
"""


def triangle(board): 
    # your code goes here:
    width = len(board)
    height = len(board[width-1])
    resultBoard = [[100]* (height+1) for i in range(width+1)]
    for i in range(1,len(board)+1):
        height = len(board[i-1])
        for j in range(1,height+1):
            if i == 1:
                resultBoard[i][j] = board[i-1][j-1]
            elif j == 1:
                resultBoard[i][j] = resultBoard[i-1][j] + board[i-1][j-1]
            elif j == height:
                resultBoard[i][j] = resultBoard[i-1][j-1] + board[i-1][j-1]
            else:
                resultBoard[i][j] = min(resultBoard[i-1][j], resultBoard[i-1][j-1]) + board[i - 1][j - 1]
    return min(resultBoard[width])



    


if __name__ == "__main__":
    board = [[2],[5,4],[1,4,7],[8,6,9,6]]
    print(triangle(board))


