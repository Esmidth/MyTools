#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
import sys

print sys.argv
List1 = []


def printpart():
    global List1
    # rename1()
    print "---------------------------------PREVIEW----------------------------------------"
    # print "Original File Names".ljust(49),"New File Names"
    m = 0
    while m < len(List):
        print m + 1, "\t%s" % (List[m]).ljust(90), "--->>--" + "\t\t%s.%s" % (List1[m], Type)
        m += 1
    print "---------------------------------END--------------------------------------------"
    print "    printpart()\n    remove(From,To)\n    rename(Number)\n    do()"


def remove(fromm, to):
    global List, List1
    while fromm <= to:
        del List[fromm - 1]
        to -= 1
    printpart()
    # return List


def rename1():
    global List1, List
    if len(List) < 10:
        List1 = map(lambda x: Name % (Season, "0%s" % x),
                    range(1, len(List) + 1))  # Name格式中带有%s，因此直接用％（）可以替换掉其中的数据，符合输出格式
    else:
        List1 = map(lambda x: Name % (Season, "0%s" % x), range(1, 10))
        List1.extend(map(lambda x: Name % (Season, x), range(10, len(List) + 1)))
    # return List1


def do():
    i = 0
    while i < len(List):
        shutil.move("%s%s" % (Path, List[i]), "%s%s.%s" % (Path, List1[i], Type))
        i += 1
    printpart()
    print "Done"


def rename(num):
    global List1
    print "Input the form of the file", " 'No'", num
    namem = raw_input()
    List1[num - 1] = namem
    printpart()
    # return List1


# 输入数据部分
Path = raw_input("Please input the path\n")
Name = raw_input("Input the form of the name\nFor example:\nElementary.S%sE%s.720p.WEB-DL.DD5.1.H.264-ECI.DivX\n")
Season = raw_input("Please input the Season you are editing\n")
Type = raw_input("Please input the Type of the Files\n")

Path = "%s" % Path
Path += '\\'


# 剔除掉数组数据中无用的数据
List = sorted(os.listdir("%s" % Path))
c = 0
while c < len(List):
    if List[c].find('.%s' % Type) == -1:
        del List[c]
        c = 0
    else:
        c += 1
rename1()
printpart()