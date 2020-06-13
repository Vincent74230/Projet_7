#coding : UTF-8
import requests
import os

print (os.environ.get('API_KEY'))


class Get_position:
    '''class that fetches lontitude and latitude of a place in the world, returns a json'''
    def send_request(self, place_in_the_world):
        payload = {'address':place_in_the_world, 'key':os.environ.get('API_KEY')}
        response = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=payload)
        if response.status_code == 200:
            try:
                response = response.json()
                response = response['results'][0]
                return {'address':response['formatted_address'], 'position':response['geometry']['location']}
            except Exception:
                return None
