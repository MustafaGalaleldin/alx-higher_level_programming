#!/usr/bin/python3
'''
a Python script that fetches
https://alx-intranet.hbtn.io/status
'''
import urllib.request

if __name__ == '__main__':
	url = 'https://alx-intranet.hbtn.io/status'
	with urllib.request.urlopen(url) as response:
		page = response.read()
		print('Body response:')
		print('\t- type:', type(page))
		print('\t- content:', page)
		print('\t- utf8 content:', page.decode('utf-8'))
