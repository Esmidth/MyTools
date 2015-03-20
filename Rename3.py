#!/usr/local/bin/python3
'''
Created on 2012-4-4

@author: Esmidth

'''
import os
import shutil

#输入数据部分
print("Please input the path")
Path=input()

#print("Please input the numbers of the Series")
#Numbers=int(input())
  
print("Please input the name of the Series")
Name=input()

print("Please input the season you are editing")
Season=input()

print("Please input the type of the Series")
Type=input()

Path="%s" % Path
Path=Path + '\\'
    
#剔除掉数组数据中无用的数据
a=sorted(os.listdir("%s" % Path))
b=len(a)
c=0
while c < b:
        if a[c].find('.%s' % (Type))==-1 :
                del a[c]
                b=len(a)
                c=0
        else : c=c+1
                

#屏幕输出部分
print("---------------------------------PREVIEW----------------------------------------")
m=0
n=1
while m<b:
        if n<10 :
                print("%s"% (a[m])+"----->>--"+"%s S%sE0%s.%s" % (Name,Season,n,Type))
        else:   print("%s"% (a[m])+"----->>--"+"%s S%sE%s.%s" % (Name,Season,n,Type))
        m=m+1
        n=m+1   
print("---------------------------------END--------------------------------------------")
print("Do it? Y/N")
x=input()

#文件输出部分
i=0
t=1
if x == "y" or x =="Y":
        while i<b :
            if t<10 :
                shutil.move("%s%s"% (Path,a[i]),"%s%s S%sE0%s.%s" % (Path,Name,Season,t,Type))
            else :
                shutil.move("%s%s"% (Path,a[i]),"%s%s S%sE%s.%s" % (Path,Name,Season,t,Type))
            i=i+1
            t=t+1
        print("Done,thanks")
else :
        print("Cancelled")

