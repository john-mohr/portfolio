"""
    Bottom Up Solution to Stair Climbing

    [John David Mohr]
"""

def climb_stair(n):
    values = [0] * (n+1)
    values[1] = 1
    for i in range(2, n+1):
        values[i] = values[i-1] + values[i-2]
    return values[n] + values[n-1]




if __name__ == "__main__":
    print(climb_stair(10))
    print(climb_stair(20))
    print(climb_stair(30))

