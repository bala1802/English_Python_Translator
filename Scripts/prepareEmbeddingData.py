# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 13:44:56 2021

@author: balaguru.s
"""

import glob

def read(filePath):
    content = ""
    with open(filePath, 'r', encoding='utf-8') as content_file:
        content = content_file.read()
    return content

def extractFiles():
    filePaths = []
    for filePath in glob.iglob('D:\Training\END\Session14_Working\V2\Current\Scripts/*.py'):
        filePaths.append(filePath)
    return filePaths

def convertTargetToSingleLine(block) :
    lines = block.splitlines()
    newLines = ''
    for line in lines:
            if '#' in line:
                split_string = line.split('#', 1)
                line = split_string[0]
            tempLine = line.strip()
            if tempLine != '':
                num_spaces = 0
                
                for letter in line:
                    if letter != ' ':
                        break
                    num_spaces += 1
                
                if num_spaces > 0:
                    line = line.replace(' '*num_spaces, ' \t ')
                
                line = handleSpecialCharacters(line)
                newLines = newLines + ' \n ' + line
            
    converted = repr(newLines)
    return converted


def handleSpecialCharacters(line):
    specialCharacters = ['!', '”', '#', '$', '%', '&', "’", '(',  ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '\\', '^', '_', '`', '{', '|', '}', '~', '[', ']' ]
    for specialCharacter in specialCharacters:
        newSpecialCharacter = ' ' + specialCharacter + ' '
        line = line.replace(specialCharacter, newSpecialCharacter)
    return line

def writeToTextFile(allConverted, counter):
    with open('D:\Training\END\Session14_Working\V2\Current\Embedding_Files/emdedding_file_' + str(counter) + '.txt', 'w') as f:
        for converted in allConverted:
            f.write(converted)
            
            
    

def process():
    filePaths = extractFiles()
    counter = 1
    print('Total number of files : ', len(filePaths))
    for filePath in filePaths:
        content = read(filePath)
        converted = convertTargetToSingleLine(content)
        converted = converted + '\n'
        writeToTextFile(converted, counter)
        fileDone = 'emdedding_file_' + str(counter)
        print('Done with : ', fileDone)
        counter = counter + 1
        
    return 

process()