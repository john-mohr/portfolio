"""
    inversion.py
    Implementation of two algorithms to find the 
    number of inversions in an array of n integers

    [John David Mohr]
"""



# Brute Force, O(n^2)
def count_inversion_BF(num):
     # your code goes here:
     sum = 0
     for i in num:
         for j in range(num.index(i) + 1 ,len(num)):
             if i > num[j]:
                sum += 1

     return sum

# Divide and Conquer, O(nlogn)
def count_inversion_DnC(num):
    # your code goes here:
    if len(num) == 1:
        return num, 0
    else:
        left, sumLeft = count_inversion_DnC(num[:int(len(num)/2)])
        right, sumRight = count_inversion_DnC(num[int(len(num)/2):])
        sum = sumLeft + sumRight
        i, j = 0,0
        temp = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
            sum += len(left) - i
    temp += left[i:]
    temp += right[j:]
    return temp, sum

if __name__ == "__main__":

    num = [3,6,8,9,0,1,34,56,73,23,345,65,37,25]

    print("Brute Force: ", count_inversion_BF(num))
    print("Divide and Conque: ", count_inversion_DnC(num))

        