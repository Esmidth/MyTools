__author__ = 'Esmidth'

import time


def merge(A, p, q, r):
    b = A[p:q]
    b.append('N')
    c = A[q:r]
    c.append('N')
    m = 0
    n = 0
    while b[m] != 'N' and c[n] != 'N':
        if b[m] < c[n]:
            A[p] = b[m]
            m += 1
        else:
            A[p] = c[n]
            n += 1
        p += 1
    if p >= len(A):
        return 0
    if m > n:
        A[p] = c[n]
    else:
        A[p] = b[m]





b = [5, 2, 4, 6, 1, 3, 9, 7, 8, 10, 12, 14, 18, 17, 11, 13, 20, 16, 19, 15]
a = b.copy()
i = 0

time_start = time.time()

while i < len(a) - 1:
    if a[i] > a[i + 1]:
        temp = a[i]
        a[i] = a[i + 1]
        a[i + 1] = temp
        i -= 2
        if i < 0:
            i = -1
    i += 1
print(a)
time_end = time.time()

print("Insertion-sort(A): ", time_end - time_start)

a = b.copy()
j = 1
time_start = time.time()

while j < len(a):
    i = j - 1
    temp = a[j]
    while i >= 0 and temp < a[i]:
        a[i + 1] = a[i]
        i -= 1
    a[i + 1] = temp
    j += 1
print(a)
time_end = time.time()
print("B: ", time_end - time_start)



a = b.copy()
time_start = time.time()
if len(a) % 2 == 0:
    i = 1
    p = 0
    r = 0
    while i * 2 <= len(a):
        while r <= len(a):
            q = p + i
            r = q + i
            merge(a, p, q, r)
            p += (i * 2)
        p = 0
        r = 0
        i *= 2
time_end = time.time()
print("C: ", time_end - time_start)
print(a)