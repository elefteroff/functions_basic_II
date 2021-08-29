# Countdown:

def countdown(num):
    y = []
    for x in range(num, -1, -1):
        y.append(x)
    print(y)
countdown(10)



#Print and Return

def printReturn(a):
    print(a[0])
    return a[1]
printReturn([6,7])


#First Plus Length:

def firstPlusLength(a):
    sum = a[0] + len(a)
    print(sum)

firstPlusLength([10,12,14,16])
    

#Values Greater than Second:


def valGreat(a):
    y = [] 
    count = 0
    for x in range (0, len(a), 1):
        # print(x)
        if a[x] > a[1]:
            # global count
            count += 1
            y.append(a[x])
    print(count)
    print(y)

valGreat([1,2,3,4,5])


#This Length, That Value:


def thisThat(size,value):
    y  = []
    for x in range (0, size):
        y.append(value)
    print(y)

thisThat(4,7)