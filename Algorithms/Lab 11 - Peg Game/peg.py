from copy import deepcopy as copy
import argparse
from animation import draw

class Node():
    def __init__(self, board, jumpfrom = None, jumpover = None, jumpto = None):
        self.board = board
        self.jumpfrom = jumpfrom
        self.jumpover = jumpover
        self.jumpto = jumpto

class peg:
    def __init__(self, start_row, start_col, rule):
        self.size = 5
        self.start_row, self.start_col, self.rule = start_row, start_col, rule
        # board
        self.board = [[1 for j in range(i+1)] for i in range(self.size)]
        self.board[start_row][start_col] = 0
        self.start = Node(copy(self.board))
        # path
        self.path = []

        # Do some initialization work here if you need:



    def draw(self):
        if self.success(self.board):
            draw(self.path, self.start_row, self.start_col, self.rule)
        else:
            print("No solution were found!")


    def success(self,board):
        # your code goes here:
        return sum(sum(board, [])) == 1


    def get_empty_positions(self,board,path):

        # If board has only 1 peg left set self.board to the solution
        if self.success():
            self.path = path
            self.board = board
            return True


        emptyPos = []
        for i in range(self.size):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    emptyPos.append((i,j))

        return False
        for i in emptyPos:
            self.getJumps(i[0],i[1],board,path)


    def getJumps(self,x,y,board):
        jumps = (x-2,y-2),(x-2,y),(x,y-2),(x+2,y),(x,y+2),(x+2,y+2)
        boardJumps = board
        validJumps = []

        for j in range(len(jumps)):
            for i in range(len(boardJumps)):
                if (jumps[j][0] <= len(boardJumps)-1 and jumps[j][0] >= 0) and (jumps[j][1] <= len(boardJumps[jumps[j][0]])-1 and jumps[j][1] >= 0):
                    if jumps[j] not in validJumps and boardJumps[jumps[j][0]][jumps[j][1]] == 1:
                        validJumps.append(jumps[j])

        if(len(validJumps)==0):
            return []

        return validJumps



    def solve(self, board = None, level = 0):
        # your code goes here
        if board == None:
            board = copy(self.board)

        if self.success(board):
            self.board = board
            return True

        jumpTo = []
        for i in range(self.size):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    jumpTo.append((i, j))

        for i in jumpTo:
            jumpFrom = self.getJumps(i[0],i[1],board)
            # print(jumpFrom)

            for j in jumpFrom:
                # if level >= 6:
                # print("")
                boardTemp = copy(board)
                jumpOver = int(j[0] + ((i[0] - j[0]) / 2)),int(j[1] + ((i[1] - j[1]) / 2))
                if boardTemp[jumpOver[0]][jumpOver[1]] == 1:
                    boardTemp[i[0]][i[1]] = 1;
                    boardTemp[jumpOver[0]][jumpOver[1]] = 0
                    boardTemp[j[0]][j[1]] = 0

                    # print(i, j, (int(j[0] + (i[0] - j[0]) / 2), int(j[1] + (i[1] - j[1]) / 2)))
                    # if level == 8 and boardTemp[1] == [0,1] and boardTemp[4] == [1,1,0,0,1] and boardTemp[3]== [0,0,1,0]:
                    # if level == 11 and boardTemp[4] == [0, 0, 0, 0, 1] and boardTemp[3] == [0,0,0,1]:
                    if level == 12 and boardTemp[2] == [0, 0, 1]:
                        print(level, boardTemp, sum(sum(boardTemp, [])))
                    self.path.append(Node(copy(boardTemp), j, jumpOver,i))
                    if self.solve(boardTemp,level+1):
                        return True
                    else: self.path.pop()

        return False




if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='peg game')

    parser.add_argument('-hole', dest='position', required = True, nargs = '+', type = int, help='initial position of the hole')
    parser.add_argument('-rule', dest='rule', required = True, type = int, help='index of rule')

    args = parser.parse_args()

    start_row, start_col = args.position
    if start_row > 4:
        print("row must be less or equal than 4")
        exit()
    if start_col > start_row:
        print("column must be less or equal than row")
        exit()

    # Example:
    # python peg.py -hole 0 0 -rule 0
    game = peg(start_row, start_col, args.rule)
    game.solve()
    game.draw()
