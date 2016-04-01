#Author: Benjamin Cecile
#Created: January 23, 2016
#
#Gets all of the itemUrl[0], itemUrl[1]s and accessories info from the InflationRPG wiki
#

from lxml import html
import requests

allUrl = ['http://inflation-rpg.wikia.com/wiki/Armors',
          'http://inflation-rpg.wikia.com/wiki/Weapons',
          'http://inflation-rpg.wikia.com/wiki/Accessories']

itemNames = ['Armors', 'Weapons', 'Accessories']

itemUrl = [[], [], []]
itemTree = [[], [], []]

for i in range(3):
    itemUrl[i] = requests.get(allUrl[i])
    itemTree[i] = html.fromstring(itemUrl[i].text)
    currentTree = html.tostring(itemTree[i].getroottree())
    outFile = open(itemNames[i]+'.html', 'w')
    
    itemHTML = ''
    currentLine = ''
    depth = 0
    startTable = False
    linkDelete = False
    for j in range(len(currentTree)):
        #Gets a line until a newline character
        currentLine += chr(currentTree[j])
        if ('>' in currentLine):
            #Finds the specific table I want
            if ('<table class' in currentLine):
                #Set the new style
                if ('style=' in currentLine):
                    currentLine = currentLine[0:currentLine.find('style=')+7] + 'background-color: #eee; text-align: center; border: 2px solid black;border-collapse: collapse;' + currentLine[currentLine.index('"', currentLine.find('style=')+7):len(currentLine)]
                else:
                    currentLine = currentLine[0:len(currentLine)-1] + 'style="background-color: #eee; text-align:center; border: 2px solid black; border-collapse; collapse"' + currentLine[len(currentLine)-1]
                if ('border=' in currentLine):
                    currentLine = currentLine.replace('border="0"', 'border="1"')
                startTable = True
            if (startTable == True):
                if ('background-color' in currentLine and '<table class' not in currentLine):
                    backIndex = currentLine.find('background-color')
                    nextIndex = currentLine.index('"', backIndex)
                    if (';' in currentLine):
                        semiIndex = currentLine.find(';', backIndex)
                    if (nextIndex > semiIndex and semiIndex != -1):
                        nextIndex = semiIndex
                    currentLine = currentLine[0:backIndex] + currentLine[nextIndex:len(currentLine)]
                if ('<a' in currentLine):
                    linkDelete = True
                if (linkDelete == False):
                    if ('</' in currentLine):
                        depth -= 1
                    elif ('<' in currentLine and '<!' not in currentLine and "<img" not in currentLine):
                        depth += 1
                else:
                    if ('</a>' in currentLine):
                        linkDelete = False
                    #Delete everything from '<' to '>'
                    currentLine = currentLine.replace(currentLine[currentLine.find('<'):len(currentLine)], '')
                itemHTML += currentLine
                #print(depth, end='\t')
                if ('</table>' in currentLine and depth == 0):
                    startTable = False
                    break
            currentLine = ''
    print(itemHTML, file=outFile)
    outFile.close()
