"""
    puzzle.py
    Solves a tromino puzzle

    [John David Mohr, Thor Madsen]
"""
import matplotlib.pyplot as plt
import argparse


class puzzle:

    def __init__(self, size, block):
        # size is the size of board.
        # block is the position (x,y) of the block

        # fill the initial block as black
        self.fill_one_square(block, 'k')
        # draw the board
        self.grid(size)
        # solve it
        self.solve(block, 1, size, 1, size)
        # save and show
        self.save_and_show(size, block)

    # solve the puzzle with a block at board[left, right, bottom, top]
    def solve(self, block, left, right, bottom, topr):
        # You should recursively call solve() on four small size boards with only one block on each board
        # You should stop the recursive call when reaching to a base case which is board 2*2
        # You only need to call get_quadrant() and fill_L() in this function,
        #       where fill_L() is provided but get_quadrant() is not.

        # Your code goes here:
        quad = self.get_quadrant(block, left, right, bottom, topr)

        cr, cc = ((topr + bottom) // 2), ((right + left) // 2)
        self.fill_L(quad, left, right, bottom, topr)
        if right - left <= 2 and topr - bottom <= 2:
            pass
        else:
            if (quad == 1):
                self.solve(block, cc + 1, right, cr + 1, topr)
                self.solve([cc, cr + 1], left, cc, cr + 1, topr)
                self.solve([cc, cr], left, cc, bottom, cr)
                self.solve([cc + 1, cr], cc + 1, right, bottom, cr)

            elif (quad == 2):
                self.solve([cc + 1, cr + 1], cc + 1, right, cr + 1, topr)
                self.solve(block, left, cc, cr + 1, topr)
                self.solve([cc, cr], left, cc, bottom, cr)
                self.solve([cc + 1, cr], cc + 1, right, bottom, cr)

            elif (quad == 3):
                self.solve([cc + 1, cr + 1], cc + 1, right, cr + 1, topr)
                self.solve([cc, cr + 1], left, cc, cr + 1, topr)
                self.solve(block, left, cc, bottom, cr)
                self.solve([cc + 1, cr], cc + 1, right, bottom, cr)

            elif (quad == 4):
                self.solve([cc + 1, cr + 1], cc + 1, right, cr + 1, topr)
                self.solve([cc, cr + 1], left, cc, cr + 1, topr)
                self.solve([cc, cr], left, cc, bottom, cr)
                self.solve(block, cc + 1, right, bottom, cr)

    # return the quadrant of the block at board[left, right, bottom, top]
    def get_quadrant(self, block, left, right, bottom, topr):
        if block[0] >= ((right - left + 1)/2)+left:
            if block[1] >= ((topr-bottom+1)/2)+bottom:
                return 1
            else:
                return 4
        else:
            if block[1] < ((topr-bottom+1)/2)+bottom:
                return 3
            else:
                return 2





    # fill a L at the center of board[left, right, bottom, top]
    def fill_L(self, quadrant, left, right, bottom, topr):
        # cr is row of the center
        # cc is column of the center
        cr, cc = (topr + bottom) // 2, (right + left) // 2
        # L of type 1
        if quadrant == 1        :
            self.fill_one_square((cr, cc), 'r')
            self.fill_one_square((cr, cc + 1), 'r')
            self.fill_one_square((cr + 1, cc), 'r')
        # L of type 2
        elif quadrant == 2:
            self.fill_one_square((cr, cc), 'b')
            self.fill_one_square((cr, cc + 1), 'b')
            self.fill_one_square((cr + 1, cc + 1), 'b')
        # L of type 3
        elif quadrant == 3:
            self.fill_one_square((cr, cc + 1), 'g')
            self.fill_one_square((cr + 1, cc), 'g')
            self.fill_one_square((cr + 1, cc + 1), 'g')
        # L of type 4
        elif quadrant == 4:
            self.fill_one_square((cr, cc), 'y')
            self.fill_one_square((cr + 1, cc), 'y')
            self.fill_one_square((cr + 1, cc + 1), 'y')

    # fill one square at postion (x,y) in color
    def fill_one_square(self, position, color):
        x, y = self.get_xy_coordinate(position)
        plt.fill(x, y, color)

    # position is (i,j)
    # return [x1,x2,x3,x4], [y1,y2,y3,y4]
    def get_xy_coordinate(self, position):
        r1, r2 = position[0] - 1, position[0]
        c1, c2 = position[1] - 1, position[1]
        return [c1, c2, c2, c1], [r1, r1, r2, r2]

    # draw the board
    def grid(self, size):
        for row in range(size + 1):
            x = [i for i in range(size + 1)]
            for col in range(size + 1):
                y = [col for i in range(size + 1)]
                plt.plot(x, y, 'k')

        for col in range(size + 1):
            y = [i for i in range(size + 1)]
            for row in range(size + 1):
                x = [col for i in range(size + 1)]
                plt.plot(x, y, 'k')

    # save and show the solution
    def save_and_show(self, size, block):
        plt.axis("off")
        plt.axis('equal')
        plt.title("puzzle")
        plt.savefig("result_size_" + str(size) + "_block_" + str(block[0]) + "_" + str(block[1]) + ".png")
        plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='puzzle')

    parser.add_argument('-size', dest='size', required=True, type=int, help='size of the board: 2^n')
    parser.add_argument('-block', dest='block', required=True, nargs='+', type=int,
                        help='position of the initial block')

    args = parser.parse_args()

    # size is the size of board. size must be a positive integer 2^n like 2, 4, 8, 16.
    # block is the initial position (x,y) of the missing square. block must be two integers between 1 and size
    # run this code in terminal like this: python puzzle.py -size 8 -block 1 1
    game = puzzle(args.size, tuple(args.block))

