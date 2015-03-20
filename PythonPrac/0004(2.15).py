__author__ = 'Esmidth'

path = "/Users/Esmidth/carinfo.txt"

a = open(path)
b = a.read()

b = b.replace('\n', ' ')
b = b.lower()

c = []
origin_copy = b

while (b.find(' ')) != -1:
    c.append(b[:b.find(' ')])
    b = b[b.find(' ') + 1:]

for i in c:
    if c.count(i) != 1:
        del c[c.index(i)]

for i in c:
    print(i, origin_copy.count(i))

