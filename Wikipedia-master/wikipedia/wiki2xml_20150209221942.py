import os
import xml.dom.minidom
import codecs
import wikipedia


NameList = []


def printpart():
    print("---------------------------------PREVIEW----------------------------------------")
    m = 0
    while m < len(NameList):
        print(m + 1, "\t%s" % (NameList[m]).ljust(90))
        m += 1
    print("---------------------------------END--------------------------------------------")


def remove(From, to):
	global NameList
	while From <= to:
		del NameList[From - 1]
		to -= 1
	printpart()


def set_source_path():
	global source_path
	source_path = input("Please input the source_path\n")
	source_path += '\\'
	scan(source_path)


def scan(source_path):
	global NameList
	NameList = sorted(os.listdir(source_path))
	temp = 0
	while temp < len(NameList):
		if NameList[temp].find('[') == -1:
			del NameList[temp]
			temp = 0
		else:
			temp += 1


def save():
	domcopy = dom.cloneNode(True)
	# _Indent_(domcopy,domcopy.documentElement)
	f = open(XMLPath, 'wb')
	writer = codecs.lookup('utf-8')[3](f)
	domcopy.writexml(writer, encoding='utf-8')
	domcopy.unlink()
	print("Done")


def _search_wiki(title, lang):
	wikipedia.set_lang(lang)
	temp = wikipedia.page(title)
	return temp


def _xml_init():
	global XMLPath
	global root
	XMLPath = input("")
	dom = xml.dom.minidom.parse(XMLPath)
	root = dom.documentElement


def _addele_(Element, TextNode):
	item = dom.createElement(Element)
	text = dom.createTextNode(TextNode)
	item.appendChild(text)
	return item


# def _Indent_(dom,node,indent = 0):
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
def _add_anime(name, summary, content, images, lang):
	anime_name = _addele_(name, name)
	anime_summary = _addele_(summary, summary)
	anime_content = _addele_(content, content)
	anime_images = _addele_(images, images)
	anime_name.appendChild(anime_summary)
	anime_name.appendChild(anime_content)
	anime_name.appendChild(anime_images)
	root.appendChild(anime_name)


def _init_():
	global NameList
	_xml_init()
	set_source_path()
	scan(source_path)
	printpart()


def do():
	i = 0
	while len(NameList) > i:
		m = NameList[i].find('[')
		n = NameList[i].find(']')
		title = NameList[i][m + 1:n]
		temp_page = _search_wiki(title, 'zh')
		_add_anime(temp_page.title, temp_page.summary, temp_page.content, temp_page.images, 'zh')
		i += 1
	save()


_init_()
