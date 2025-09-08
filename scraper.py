from bs4 import BeautifulSoup
import json

with open("alt.html") as f:
    soup = BeautifulSoup(f, 'html.parser')
    for sup in soup.find_all('sup'):
        sup.extract()
    for speaker in soup.find_all('a'):
        if speaker.get('aria-label'):
            speaker.extract()
    glossary = {}
    for dl in soup.find_all('dl'):
        word = ""
        definition = ""
        for child in dl.children:
            if child.name == "dt":
                glossary[word]                
    #with open("alt.json", 'w') as g:
    #    json.dump(glossary,g,indent=4)
