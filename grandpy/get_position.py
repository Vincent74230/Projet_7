#coding : UTF-8
import requests

def get_position(location):
    payload = {'address':location,'key':'AIzaSyBvjVqsDCXUG3xGNdZai3lQBkekuMbUAfk'}
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=payload)

    print(r.url)
    r = r.json()
    r = r['results']
    print(r)
    print(r[1])


get_position('paris')