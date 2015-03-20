#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
run with python 2.x 
@by Esmidth
'''
import random

a = [0, 0, 0, 0]
b = [0, 0, 0, 0]
c = [0, 0, 0, 0]
d = [0, 0, 0, 0]
e = [a, b, c, d]


def random_z():
    x = random.randint(0, 3);
    y = random.randint(0, 3)
    while e[x][y] != 0:
        x = random.randint(0, 3);
        y = random.randint(0, 3)
    e[x][y] = random.choice([2, 4])
    return e


def printpart():
    a1 = [str(a[0]), str(a[1]), str(a[2]), str(a[3])]
    b1 = [str(b[0]), str(b[1]), str(b[2]), str(b[3])]
    c1 = [str(c[0]), str(c[1]), str(c[2]), str(c[3])]
    d1 = [str(d[0]), str(d[1]), str(d[2]), str(d[3])]
    e1 = [a1, b1, c1, d1]
    # x00=str(e[0][0]);x01=str(e[0][1]);x02=str(e[0][2]);x03=str(e[0][3])
    # x10=str(e[1][0]);x11=str(e[1][1]);x
    print "|-------|-------|-------|-------|"
    print "|'%s"


def cal():


def right():
    x = 0
    while x < 3:
        y = 0
        while y < 3:
            if e[x][y] == e[x][y + 1]:  # 相邻的右移(相等)
                e[x][y + 1] = e[x][y] + e[x][y + 1]
                e[x][y] = 0
                y = -1
            if e[x][y + 1] == 0:  # 不相邻的右移（间隔1/不相等）
                if e[x][y + 2] == 0:  #间隔2/不相等
                    e[x][y + 2] = e[x][y]
                    e[x][y] = 0
                else:
                    e[x][y + 1] = e[x][y]
                    e[x][y] = 0
                y = -1
            y = y + 1
        x = x + 1


def down():
    y = 0
    while y < 3:
        x = 0
        while x < 3:
            if e[x][y] == e[x + 1][y]:  # 相邻的下移
                e[x + 1][y] = e[x][y] + e[x + 1][y]
                e[x][y] = 0
                x = -1
            if e[x + 1][y] == 0:  # 不相邻的下移（间隔1）
                if e[x + 2][y] == 0:
                    e[x + 2][y] = e[x][y]
                    e[x][y] = 0
                else:
                    e[x + 1][y] = e[x][y]
                    e[x][y] = 0
                x = -1
            x = x + 1
        y = y + 1


def left():  # 左移函数从左向右扫
    x = 3
    while x > -1:
        y = 3
        while y > -1:
            if e[x][y] == e[x][y - 1]:  # 相邻的左移(相等)
                e[x][y - 1] = e[x][y] + e[x][y - 1]
                e[x][y] = 0
                y = 4
            if e[x][y - 1] == 0:  # 不相邻的左移（间隔1/不相等）
                if e[x][y - 2] == 0:  # 间隔2/不相等
                    e[x][y - 2] = e[x][y]
                    e[x][y] = 0
                else:
                    e[x][y - 1] = e[x][y]
                    e[x][y] = 0
                y = 4
            y = y - 1
        x = x - 1
