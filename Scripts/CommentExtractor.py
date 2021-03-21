# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:06:30 2021

@author: balaguru.s
"""

'''
Read Dataset from the text file
'''
import os

def readDataSet(filePath):
    content = ""
    with open(filePath, 'r', encoding='utf-8') as content_file:
        content = content_file.read()
    return content

def extractComments(content):
    lines = content.splitlines()
    comments = []
    for line in lines:
        tempLine = line.strip()
        if tempLine.startswith('#'):
            comments.append(line)
                            
    return comments

def writeToFile(lines):
    with open('D:\Training\END\Session14/comments.txt', 'a', encoding='utf-8') as f1:
        for line in lines:
            if line != '':
                f1.write(line + os.linesep)

content = readDataSet("D:\Training\END\Session14/english_python_data_original.txt")
lines = extractComments(content)
writeToFile(lines)