#coding : UTF-8
import requests

def get_position(place_in_the_world):
    '''class that fetches lontitude and latitude of a place in the world, returns a json'''
    payload = {'address':place_in_the_world, 'key':'AIzaSyBvjVqsDCXUG3xGNdZai3lQBkekuMbUAfk'}
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=payload)
    if response.status_code == 200:
        try:
            response = response.json()
            response = response['results'][0]
            return {'address':response['formatted_address'], 'position':response['geometry']['location']}
        except Exception:
            return None
