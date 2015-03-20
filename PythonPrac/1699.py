__author__ = 'Esmidth'

n = int(input())

i = 0
while i < n:
    i1 = 0
    d = []
    n1 = int(input())
    while i1 < n1:
        d.append(input())
        i1 += 1
    i1 = 0
    while i1 < n1-1:
        if d[i1] > d[i1+1]:
            temp = d[i1]
            d[i1] = d[i1+1]
            d[i1+1] = temp
            i1 = 0
        i1 += 1
    for ele in d:
        print(d[ele])
    i += 1
