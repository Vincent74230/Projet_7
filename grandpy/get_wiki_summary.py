#coding utf-8

import requests

def get_wiki_summary ():
    payload= {'action':'query', 'prop':'extract', 'format':'json', 'titles': 'paris'}
    response = requests.get('https://en.wikipedia.org/w/api.php',params=payload)
    response = response.json()

    return response

print(get_wiki_summary())


https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=Stack%20Overflow




"""
S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

SEARCHPAGE = "gizeh pyramid"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "search",
    "srsearch": SEARCHPAGE
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

if DATA['query']['search'][0]['title'] == SEARCHPAGE:
    print("Your search page '" + SEARCHPAGE + "' exists on English Wikipedia")

print (DATA)
"""