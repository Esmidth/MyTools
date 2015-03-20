#!/usr/local/bin/python3
'''
Created on 2012-4-4

@author: Esmidth

'''

import os
import shutil
import string

print("Please input the path")
Path=input()

print("Please input the name of the first file")
Name=input()

print("Please input the season you are editing")
Season=input()

print("Please input the numbers of the Series")
Numbers=int(input())

Numbers=Numbers+1

Name="%s" % Name

Path="%s" % Path
Path=Path + '\\'

b=Name

#a=sorted(os.listdir("%s" % Path))

i=1

while i<Numbers :
    #d=b.replace("01","0")
    if i<10 :
        d=b.replace("01","0%s" % (i),1)
        c=d.replace("0%s" % (i),"S%sE0%s" % (Season,i),1)
    else :
        d=b.replace("01","%s" % (i),1)
        c=d.replace("%s" % (i),"S%sE%s" % (Season,i),1)
    shutil.move("%s%s" % (Path,d),"%s%s " % (Path,c))
    #print(Path,c,d)
    i=i+1
print("Done,thanks")
input()


