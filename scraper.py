from bs4 import BeautifulSoup
import json
import requests

api_url = "https://en.wikipedia.org/api/rest_v1/page/html/Glossary_of_2020s_slang"
headers = {"User-Agent": "WikiGlossaries/0.0.1 (Zeitungsleser@GitHub) requests"}
html = requests.get(api_url, headers=headers, timeout=15).text

soup = BeautifulSoup(html, 'html.parser')
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

with open("slang.json", 'w') as g:
    json.dump(glossary,g,indent=4)
