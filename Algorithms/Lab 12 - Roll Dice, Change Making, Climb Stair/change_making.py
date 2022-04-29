"""
    Dynamic Programming Solution to Change Making Problem
    Bottom Up Solution

    [John David Mohr]
"""


def change_making(d,n):
    # Your code goes here:
    values = [0] * (n + 1)
    for i in range(1, n+1):
        temp = []
        for j in d:
            if i >= j:
                temp.append(values[i-j]+1)
        values[i] = (min(temp))
    return values[-1]





if __name__ == "__main__":
    d=[1,3,4,5,6]
    n=10
    print(change_making(d,n))
    
    d=[1,2,4,6,8,10,22,23]
    n=40
    print(change_making(d,n))

    d=[1,2,10,11,12,15,19,30]
    n=1900
    print(change_making(d,n))

