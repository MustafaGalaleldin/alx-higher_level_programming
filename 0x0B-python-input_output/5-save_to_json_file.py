#!/usr/bin/python3
'task 5'


import json


def save_to_json_file(my_obj, filename):
    'save_to_json_file'
    with open(filename, mode='w', encoding='UTF8') as f:
        f.write(json.dumps(my_obj))
