#!/usr/bin/python3
'6th task'


import json


def load_from_json_file(filename):
    'load_from_json_file'
    with open(filename, mode='r', encoding='UTF8') as f:
        return json.load(f)
