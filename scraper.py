from bs4 import BeautifulSoup
import json

with open("alt.html") as f:
    soup = BeautifulSoup(f, 'html.parser')
    for sup in soup.find_all('sup'):
        sup.extract()
    for speaker in soup.find_all('a'):
        if speaker.get('aria-label'):
            speaker.extract()
    words = []
    descriptions = []
    glossary = {}
    for dt in soup.find_all('dt'):
        words.append(dt.get_text().replace(" )", ")"))
    for dd in soup.find_all('dd'):
        descriptions.append(dd.get_text())
    for i, word in enumerate(words):
        glossary[word] = descriptions[i]
    with open("alt.json", 'w') as g:
        json.dump(glossary,g,indent=4)
