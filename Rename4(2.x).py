#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import shutil

# 输入数据部分
print "Please input the path"
Path = raw_input()

# print("Please input the numbers of the Series")
# Numbers=int(input())

print "Please input the name of the Series"
Name = raw_input()

print "Please input the season you are editing"
Season = raw_input()

print "Please input the type of the Series"
Type = raw_input()

Path = "%s" % Path
Path += '\\'

# 剔除掉数组数据中无用的数据
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
# 排序数据长度，剔除不符合的数据
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

# 屏幕输出部分
print "---------------------------------PREVIEW----------------------------------------"
m = 0
n = 1
while m < b:
    if n < 10:
        print "%s" % (a[m]) + "----->>--" + "%s S%sE0%s.%s" % (Name, Season, n, Type)
    else:
        print "%s" % (a[m]) + "----->>--" + "%s S%sE%s.%s" % (Name, Season, n, Type)
    m += 1
    n = m + 1
print "---------------------------------END--------------------------------------------"
print "Do it? Y/N"
x = raw_input()

# 文件输出部分
i = 0
t = 1
if x == "y" or x == "Y":
    while i < b:
        if t < 10:
            shutil.move("%s%s" % (Path, a[i]), "%s%s S%sE0%s.%s" % (Path, Name, Season, t, Type))
        else:
            shutil.move("%s%s" % (Path, a[i]), "%s%s S%sE%s.%s" % (Path, Name, Season, t, Type))
        i += 1
        t += 1
    print "Done,thanks"
else:
    print "Cancelled"