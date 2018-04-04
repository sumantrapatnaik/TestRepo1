# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
from bs4 import BeautifulSoup

main_dir = "/"


class XMLParser(object):
    def _init_(self,xml_dir):
        file_paths1 = os.listdir(xml_dir)
        file_paths = [xml_dir + "/" + x for x in file_paths1]
        
    def updateEnFile(self,filepath):
        self.xmlFilePath = filepath
        infile = open(self.xmlFilePath,"r")
        contents = infile.read()
        self.soup = BeautifulSoup(contents,'xml')
        



