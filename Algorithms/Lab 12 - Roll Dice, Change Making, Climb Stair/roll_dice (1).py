"""
    Dynamic Programming Solution to Dice Rolling 

    [John David Mohr]
"""

def roll_dice(n,m):
    rolls = [[0] * (m + 1) for i in range(n+1)]

    for i in range(1, min(7, m+1)):
        rolls[1][i] = 1

    for i in range(2, n+1):
        for j in range(1, m+1):
            for k in range(1, min(7,j)):
                rolls[i][j] += rolls[i - 1][j - k]

    return rolls[-1][-1]




if __name__ == "__main__":
    print(roll_dice(2,7))
    print(roll_dice(3,9))
    print(roll_dice(8,24))
