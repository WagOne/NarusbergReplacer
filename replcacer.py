# -*- coding: utf-8 -*-
import re
import time
import os

def dataCheck (var):
    if len(var) != 2:
        print("Noob?")
        time.sleep(2)
        os._exit(1)
    elif not(var.isupper()):
        print("Noob?")
        time.sleep(2)
        os._exit(1)

futureLastName = input("Введите первые 2 заглавные буквы вашей фамилии: ")
dataCheck(futureLastName)
presentLastName = input("Введите первые 2 зыглавные буквы фамилии владельца: ")
dataCheck(presentLastName)

pathToProjectDir = input("Введите полный путь к папке в которой лежит проект(Путь должен иметь такой формат в котором не фигурируют индентификаторы): ")
if(presentLastName in pathToProjectDir):
   print("Noob?")
   time.sleep(2)
   os._exit(2)
projectTree = os.walk(pathToProjectDir)
listOfPathsToFiles = []  #лист для хранения путей к файлам
listOfPathsToDirs = []   #лист для хранения путей к дерикториям

for d, dirs, files in os.walk(pathToProjectDir):
    for f in files:
        path = os.path.join(d,f) # формирование адреса
        listOfPathsToFiles.append(path) # добавление адреса в список

for d, dirs, files in os.walk(pathToProjectDir):
    for f in dirs:
        path = os.path.join(d,f) # формирование адреса
        listOfPathsToDirs.append(path) # добавление адреса в список

for fileElement in listOfPathsToFiles:
    try:
        with open(fileElement, 'r', encoding = "ISO-8859-1") as readFileElement:
            l = [line.strip() for line in readFileElement]
            newContent = []
            for lineFileContent in l:
                lineFileContent = re.sub(presentLastName, futureLastName, lineFileContent)
                newContent.append(lineFileContent)
        with open(fileElement, 'w', encoding = "ISO-8859-1") as writeFileElement:
            for i in newContent:
                writeFileElement.write("{}\n".format(i))
    except IOError:
        print("KK")

for i in range(len(listOfPathsToDirs)):
    projectTree = os.walk(pathToProjectDir)
    listOfPathsToDirs = []  # список для хранения путей к дерикториям
    for d, dirs, files in os.walk(pathToProjectDir):
        for f in dirs:
            path = os.path.join(d, f)  # формирование адреса
            listOfPathsToDirs.append(path)  # добавление адреса в список
    try:
        NewNamelistOfPathsToDirs = re.sub(presentLastName, futureLastName, listOfPathsToDirs[i])
        os.rename(listOfPathsToDirs[i], NewNamelistOfPathsToDirs)
    except IOError:
        print("KK")

projectTree = os.walk(pathToProjectDir)
listOfPathsToFiles = []  #список для хранения путей к файлам

for d, dirs, files in os.walk(pathToProjectDir):
    for f in files:
        path = os.path.join(d,f) # формирование адреса
        listOfPathsToFiles.append(path) # добавление адреса в список

for fileElement in listOfPathsToFiles:
    NewNamelistOfPathsToFiles = re.sub(presentLastName, futureLastName, fileElement)
    os.rename(fileElement, NewNamelistOfPathsToFiles)

input('Press any key to exit')
