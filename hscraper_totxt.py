from bs4 import BeautifulSoup
import requests
import re
import string

searchItem = input("What tingles your sack today?\n")

url = f"http://rule34.paheal.net/post/list/{searchItem}/1"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.findAll('div', {'class': 'shm-thumb thumb'})


filePath = input(
    "Where would you like to save it my child:\n") or "/home/lilpeenieweenie/wkfolder/myCode"
names = {}
srcs = {}

def main():
    
    writeFile()


def createFile():
    try: 
        outFile = open(filePath+f'/{searchItem}.txt', 'x')
    except IOError:
        outFile = open(filePath+f'/{searchItem}.txt', 'a')
    return outFile

def splitNumbers(names):

    text = ""
    characters = []
    numbers = []

    for name in names: 
        for i in name: 
            if(i.isalpha()):
                text += i

        characters.append(text)
        charlen = len(characters)
        final = characters[charlen-1]
    return(final)

def writeFile():
    for t in tbody:
        srcs =  t.br.next_sibling['href']
        names = t.img['title']
        filteredNames = splitNumbers(names)
        
        createFile().write(f"""
{filteredNames}: 
------------------------------------------------------------------
{srcs}
    """)
    
main()