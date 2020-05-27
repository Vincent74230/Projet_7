#coding : UTF-8
import requests

def get_position(location):
    payload = {'address':location,'key':'AIzaSyBvjVqsDCXUG3xGNdZai3lQBkekuMbUAfk'}
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=payload)
    response = response.json()
    response = response['results'][0]
    return {'address':response['formatted_address'],'position':response['geometry']['location']}
