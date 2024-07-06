#!/usr/bin/python3
'''
 a Python script that takes in a URL, sends a request
 to the URL and displays the body of the response.
'''
import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.RequestException as e:
        print('Error code:', response.status_code)
