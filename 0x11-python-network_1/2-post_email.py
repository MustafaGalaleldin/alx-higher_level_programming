#!/usr/bin/python3
'''
a Python script that takes in a URL and an email,
sends a POST requestto the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
'''
import sys
import urllib.request
import urllib.parse

if __name__ == '__main__':
    url = sys.argv[1]
    inf = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(inf)
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
