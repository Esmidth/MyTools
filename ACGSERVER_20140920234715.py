#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import xml.dom.minidom,codecs,os,shutil

#initialize
#Path=raw_input('Please input the path of xml files\n')
Path='C:\Users\Esmidth\Desktop\Tools\ACGServer2.xml'
#Path1=raw_input('Please input the path of the videos\n')
Path1='Z:\\'
ListY=[];ListN=[]
ListOriginal=sorted(os.listdir(Path1))

dom=xml.dom.minidom.parse(Path)
root=dom.documentElement
ListFunction=['\nAddAnime()\n','Save()\n','CreateAnimeList()\n']
print root.toxml()
print ListFunction


def AddAnime():
  Name=raw_input("動畫名\n")
  #ChiName=raw_input('中文譯名\n')
  #ChiName=codecs.lookup('utf-8')[3](ChiName)
  #NameItem=_AddEle_("ChiName",'%s'%(ChiName))
  AnimeItem=_AddEle_(Name,Name)
  #AnimeItem.appendChild(NameItem)
  Season=input('有幾季\n')
  i=0
  while i <Season:
    Seasons=_AddSeason_(i)
    AnimeItem.appendChild(Seasons)
    i=i+1
  root.appendChild(AnimeItem)

def Save():
  domcopy=dom.cloneNode(True)
  _Indent_(domcopy,domcopy.documentElement)
  f=file(Path,'wb')
  writer=codecs.lookup('utf-8')[3](f)
  domcopy.writexml(writer,encoding='utf-8')
  domcopy.unlink()
  print 'Done'

#def SaoMiaoYingPan():
  _CreateAnimeList()
  
def _CreateAnimeList_():
  ListY=_CreateAnimeList_('1')
  ListN=_CreateAnimeList_('0') 


def _AddEle_(Element,TextNode):
  item=dom.createElement(Element)
  text=dom.createTextNode(TextNode)
  item.appendChild(text)
  return item

def _AddSeason_(i):
  print '\n第%s季' %(i+1)
  List0=['本季多少集？\n','是否觀看過？\nYes/No\n','有無字幕？\nYes/No\n','發行年份\n','分辨率\n','Vedio File Type\n','BDRIP?\nYes/No\n','Nexus?\n','製作公司\n']
  List1=['Episode','Watched','Subtitle','Year','Resolution','VideoFile','BDRIP','Nexus','Produce'] #List1與List0中的元素必須一一對應
  m=0
  Seasons="%s" %(i+1)
  Season1=_AddEle_("Season",Seasons)
  while m<len(List0): 
    x=raw_input(List0[m])
    y=_AddEle_(List1[m],x)
    Season1.appendChild(y)
    m=m+1
  return Season1

def _Indent_(dom,node,indent = 0):
  # Copy child list because it will change soon
  children = node.childNodes[:]
  # Main node doesn't need to be indented
  if indent:
    text = dom.createTextNode('\n' + '\t' * indent)
    node.parentNode.insertBefore(text, node)
  if children:
      # Append newline after last child, except for text nodes
    if children[-1].nodeType == node.ELEMENT_NODE:
         text = dom.createTextNode('\n' + '\t' * indent)
         node.appendChild(text)
         # Indent children which are elements
    for n in children:
      if n.nodeType == node.ELEMENT_NODE:
        Indent(dom, n, indent + 1)


def _CreateAnimeList_(Keyword):
  a=0
  ListKid0=[];ListKid1=[]
  while a < len(ListOriginal):
    if ListOriginal[a][0] == Keyword:
      ListKid0.append(ListOriginal[a])
    a=a+1
  b=0
  while b < len(ListKid0):
    N=ListKid0[b].find(']')
    ListKid1.append(ListKid0[b][2:N])
    b=b+1
  return ListKid1

def AddInformation(Name,Season):
  AnimeItem=_AddEle_(Name,Name)
  i=0
  while i< Season:
    Seasons=_AddSeason_(i)
    AnimeItem.appendChild(Seasons)
    i=i+1
  root.appendChild(AnimeItem)
