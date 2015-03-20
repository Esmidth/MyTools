import os
import shutil
import sys
import xml.dom.minidom
import codecs
import wikipedia

liebiao = []
def printpart():
    print ("---------------------------------PREVIEW----------------------------------------")
    m=0
    while m<len(liebiao):
        print (m+1,"\t%s"% (liebiao[m]).ljust(90))
        m = m+1
    print ("---------------------------------END--------------------------------------------")

def remove(From,To):
	global liebiao
	while From <= To:
		del liebiao[From-1]
		To = To-1
	printpart()

def set_SourcePath():
	global SourcePath
	SourcePath = input("Please input the SourcePath\n")
	SourcePath = SourcePath + '\\'
	scan(SourcePath)

def scan(SourcePath):
	global liebiao
	liebiao = sorted(os.liebiaodir(SourcePath))
	temp = 0
	while temp < len(liebiao):
		if liebiao[temp].find('[') == -1:
			del liebiao[temp]
			temp = 0
		else:
			temp = temp + 1

def Save():
	domcopy = dom.cloneNode(True)
	#_Indent_(domcopy,domcopy.documentElement)
	file = file(XMLPath,'wb')
	writer = codecs.lookup('utf-8')[3](f)
	domcopy.writexml(writer,encoding='utf-8')
	domcopy.unlink()
	print ("Done")

def _searchwiki(title,lang):
	wikipedia.set_lang(lang)
	temp = wikipedia.page(title)
	return temp



def _xmlinit():
	global XMLPath
	global root
	XMLPath = input("")
	dom  = xml.dom.minidom.parse(XMLPath)
	root = dom.documentElement

def _AddEle_(Element,TextNode):
	item = dom.createElement(Element)
	text = dom.createTextNode(TextNode)
	item.appendChild(text)
	return item

#def _Indent_(dom,node,indent = 0):
  # Copy child liebiao because it will change soon
 # children = node.childNodes[:]
  # Main node doesn't need to be indented
  #if indent:
  	#	text = dom.createTextNode('\n' + '\t' * indent)
   # 	node.parentNode.insertBefore(text, node)
  #if children:
      # Append newline after last child, except for text nodes
    #if children[-1].nodeType == node.ELEMENT_NODE:
     #    text = dom.createTextNode('\n' + '\t' * indent)
     #    node.appendChild(text)
         # Indent children which are elements
    #for n in children:
     # if n.nodeType == node.ELEMENT_NODE:
      #  Indent(dom, n, indent + 1)
def _AddAnime(Name,summary,content,images,lang):
	AnimeName=_AddEle_(Name,Name)
	AnimeSummary=_AddEle_(Summary,summary)
	AnimeContent=_AddEle_(Content,content)
	AnimeImages=_AddEle_(Images,images)
	AnimeName.appendChild(AnimeSummary)
	AnimeName.appendChild(AnimeContent)
	AnimeName.appendChild(AnimeImages)
	root.appendChild(AnimeName)
def _init_():

	global liebiao
	_xmlinit()
	set_SourcePath()
	scan(SourcePath)
	printpart()
def do():
	i = 0
	while i < len(liebiao):
		m = liebiao[i].find('[')
		n = liebiao[i].find(']')
		title = liebiao[i][m+1:n]
		temppage =_searchwiki(title,'zh')
		_AddAnime(temppage.title,temppage.summary,temppage.content,temppage.images)
		i = i + 1
	Save()

_init()
