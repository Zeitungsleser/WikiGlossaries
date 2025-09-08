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
        word = None
        definition = None
        for child in dl.children:
            if child.name == "dt":
                if word:
                    glossary[word] = definition
                definition = None
                word = child.get_text()
            elif child.name == "dd":
                if child.get_text().startswith("Main article:"):
                    pass
                elif definition:
                    definition = definition + "\n" + child.get_text()
                else:
                    definition = child.get_text()  
        if word:
            glossary[word] = definition              
    with open("alt.json", 'w') as g:
        json.dump(glossary,g,indent=4)
