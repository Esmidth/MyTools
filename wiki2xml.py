import os
import xml.dom.minidom
import codecs

import wikipedia


def printpart():
    print ("---------------------------------PREVIEW----------------------------------------")
    m = 0
    while m < len(liebiao):
        print (m + 1, "\t%s" % (liebiao[m]).ljust(90))
        m += 1
    print ("---------------------------------END--------------------------------------------")


def remove(fromm, to):
    global liebiao
    while fromm <= to:
        del liebiao[fromm - 1]
        to -= 1
    printpart()


def set_sourcepath():
    global SourcePath
    # SourcePath = input("Please input the SourcePath\n")
    SourcePath = "/Users/Esmidth/Movies"
    scan(SourcePath)


def scan(sourcepath):
    global liebiao
    liebiao = sorted(os.listdir(sourcepath))
    temp = 0
    while temp < len(liebiao):
        if liebiao[temp].find('[') == -1:
            del liebiao[temp]
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
    print ("Done")


def _search_wiki(title, lang):
    wikipedia.set_lang(lang)
    temp = wikipedia.page(title)
    return temp


def _xml_init():
    global XMLPath
    global root
    global dom
    # XMLPath = input("Please input the path of XML\n")
    XMLPath = "/Users/Esmidth/Desktop/ACGserver.xml"
    dom = xml.dom.minidom.parse(XMLPath)
    root = dom.documentElement


def _add_ele_(element, textnode):
    item = dom.createElement(element)
    text = dom.createTextNode("%s" % textnode)
    item.appendChild(text)
    return item


# def _Indent_(dom,node,indent = 0):
# Copy child liebiao because it will change soon
# children = node.childNodes[:]
# Main node doesn't need to be indented
# if indent:
# text = dom.createTextNode('\n' + '\t' * indent)
# 	node.parentNode.insertBefore(text, node)
# if children:
# Append newline after last child, except for text nodes
# if children[-1].nodeType == node.ELEMENT_NODE:
#    text = dom.createTextNode('\n' + '\t' * indent)
#    node.appendChild(text)
# Indent children which are elements
# for n in children:
# if n.nodeType == node.ELEMENT_NODE:
#  Indent(dom, n, indent + 1)
def _add_anime(name, summary, content, images, lang):
    anime_name = _add_ele_(name, name)
    anime_summary = _add_ele_("Summary", summary)
    anime_content = _add_ele_("Content", content)
    anime_images = _add_ele_("Images", images)
    anime_lang = _add_ele_("Language", lang)
    anime_name.appendChild(anime_summary)
    anime_name.appendChild(anime_content)
    anime_name.appendChild(anime_images)
    anime_name.appendChild(anime_lang)
    root.appendChild(anime_name)


def _init_():
    global liebiao
    _xml_init()
    set_sourcepath()
    scan(SourcePath)
    printpart()


def do():
    i = 0
    while i < len(liebiao):
        m = liebiao[i].find('[')
        n = liebiao[i].find(']')
        title = liebiao[i][m + 1:n]
        temp_page = _search_wiki(title, 'jp')
        _add_anime(temp_page.title, temp_page.summary, temp_page.content, temp_page.images, 'zh')
        i += 1
    save()


_init_()
do()