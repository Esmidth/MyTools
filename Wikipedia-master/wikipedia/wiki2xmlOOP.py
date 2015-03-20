__author__ = 'Esmidth'

import xml.dom.minidom
import os
import codecs
import wikipedia

NameList = []


class wiki2xml(object):
    """
    Contains data and methods to wikipedia.py
    """
    def __init__(self):
        global NameList
        global XMLPath
        global root
        XMLPath = input("Please enter the path of XML file")
        dom = xml.dom.minidom.parse(XMLPath)
        root = dom.documentElement
        set_source_path()
        scan(source_path)
        printpart()

    def set_source_path(self,source_path):
        source_path += '\\'
        scan(source_path)




