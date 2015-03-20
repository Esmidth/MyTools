__author__ = 'Esmidth'

import time


b = [5, 2, 4, 6, 1, 3, 9, 7, 8, 11, 10]
a = b
i = 0

time_start = time.time()

while i < len(a) - 1:
    if a[i] > a[i + 1]:
        temp = a[i]
        a[i] = a[i + 1]
        a[i + 1] = temp
        i = 0
    i += 1
print(a)
time_end = time.time()

print("Insertion-sort(A): ", time_end - time_start)

a = b
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
time_end = time.time()
print("B: ", time_end - time_start)
