#!/usr/bin/python3
'7th task'


import sys
import json
# save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
# load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def save_to_json_file(my_obj, filename):
    'save_to_json_file'
    with open(filename, mode='w', encoding='UTF8') as f:
        f.write(json.dumps(my_obj))


def load_from_json_file(filename):
    'load_from_json_file'
    with open(filename, mode='r', encoding='UTF8') as f:
        return json.load(f)


name = "add_item.json"
try:
    my_list = load_from_json_file(name)
except Exception:
    my_list = []
for av in sys.argv[1:]:
    my_list.append(av)
save_to_json_file(my_list, name)
