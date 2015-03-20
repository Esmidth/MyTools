
'''
Created on 2012-4-4

@author: Esmidth

'''

import os
import shutil

print("Please input the path")
Path=input()

print("Please input the season you are editing")
Season=input()

print("Please input the numbers of the Series")
Numbers=int(input())
print("Please input the name of the Series")
Name=input()

print("Please input the type of the Series")
Type=input()

Path="%s" % Path
Path=Path + '\\'

a=sorted(os.listdir("%s" % Path))
if a[0]=="Thumbs.db":
    i=1
    t=1
    Numbers=Numbers + 1
else:
    i=0
    t=1


while i<Numbers :
    shutil.move("%s%s"% (Path,a[i]),"%s%s S%sE%s.%s" % (Path,Name,Season,t,Type))
    i=i+1
    t=t+1
print("Done,thanks")



