'''one class in this module: fetches datas from wiki api'''
#coding utf-8
import requests


class Get_wiki_summary:
    '''fetches a short summary from wiki api, json format'''
    def send_request(self, place_in_the_world):
        payload = {'action':'query', 'prop': 'extracts', 'format': 'json', 
                   'titles': place_in_the_world, 'exintro': True, 'explaintext': True, 'redirects':1}
        response = requests.get('https://en.wikipedia.org/w/api.php', params=payload)
        if response.status_code == 200:
            try:
                response = response.json()
                dico = response['query']['pages']
                page_id, value = next(iter(dico.items()))
                datas = response['query']['pages'][page_id]['extract']

                return datas
            except Exception:
                return None
