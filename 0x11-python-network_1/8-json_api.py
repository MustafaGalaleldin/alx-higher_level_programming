#!/usr/bin/python3
'''
a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
'''
import sys
import requests

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        char = sys.argv[1]
    else:
        char = ''
    response = requests.post(url, {'q': char})
    try:
        jj = response.json()
        if not jj:
            print('No result')
        else:
            print('[{}] {}'.format(jj['id'], jj['name']))
    except requests.exceptions.JSONDecodeError as e:
        print('Not a valid JSON')
