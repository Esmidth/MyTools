__author__ = 'Esmidth'

# -*- coding: utf-8 -*-

import sys,cmd


class PyCDC(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)

    def help_EOF(self):
        print("Quits the program")

    def do_EOF(self, line):
        sys.exit()

    def help_walk(self):
        print("Walk cd and export into *.cdc ")

    def do_walk(self, filename):
        if filename == "":filename = input("input cdc ::")
        print("Output: %s" % filename)

    def help_dir(self):
        print("")

    def do_dir(self, pathname):
        if "" == pathname: pathname = input("input path:")

    def help_find(self):
        print("Search keyword")

    def do_find(self, keyword):
        if keyword == "": keyword = input("input ")
