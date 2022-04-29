"""John David Mohr"""

def Permute(elements, n):
    if n-1 == 0:
        print(elements)
    else:
        for i in range(0,n):
            Permute(elements,n-1)
            if n%2 == 1:
                temp = elements[0]
                elements[0] = elements[n-1]
                elements[n-1] = temp
            else:
                temp = elements[i]
                elements[i] = elements[n-1]
                elements[n-1] = temp

if __name__ == '__main__':
    ele = ['a','b','c','d']
    Permute(ele, len(ele))
