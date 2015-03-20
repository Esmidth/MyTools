# -*- coding: utf-8 -*-
# !/usr/local/bin/python3

import os
import shutil

# 輸入數據部份
print("Please input the path")
Path = input()

# print("Please input the numbers of the Series")
# Numbers=int(input())

print("Please input the name of the Series")
Name = input()

print("Please input the season you are editing")
Season = input()

print("Please input the type of the Series")
Type = input()

Path = "%s" % Path
Path += '\\'

# 剔除掉數組數據中無用的數據
a = sorted(os.listdir("%s" % Path))
b = len(a)
c = 0
while c < b:
    if a[c].find('.%s' % Type) == -1:
        del a[c]
        b = len(a)
        c = 0
    else:
        c += 1
# 排序數據長度，剔除不符合的數據
c = 0
b = len(a)
Times = {}
while c < b:
    if len(a[c]) in Times:
        Times[len(a[c])] += 1
    else:
        Times[len(a[c])] = 1
    c += 1
Times2 = sorted(Times.values(), key=None, reverse=True)
Times1 = dict(map(lambda xx: (xx[1], xx[0]), Times.items()))
Length = Times1.get(Times2[0])
c = 0
b = len(a)
while c < b:
    if len(a[c]) != Length:
        del a[c]
        b = len(a)
        c -= 1
    else:
        c += 1

# 屏幕輸出部份
print("---------------------------------PREVIEW----------------------------------------")
m = 0
n = 1
while m < b:
    if n < 10:
        print("%s" % (a[m]) + "----->>--" + "%s S%sE0%s.%s" % (Name, Season, n, Type))
    else:
        print("%s" % (a[m]) + "----->>--" + "%s S%sE%s.%s" % (Name, Season, n, Type))
    m += 1
    n = m + 1
print("---------------------------------END--------------------------------------------")
print("Do it? Y/N")
x = input()

# 文件輸出部份
i = 0
t = 1
if x == "y" or x == "Y":
    while i < b:
        if 10 > t:
            shutil.move("%s%s" % (Path, a[i]), "%s%s S%sE0%s.%s" % (Path, Name, Season, t, Type))
        else:
            shutil.move("%s%s" % (Path, a[i]), "%s%s S%sE%s.%s" % (Path, Name, Season, t, Type))
        i += 1
        t += 1
    print("Done,thanks")
else:
    print("Cancelled")