import json
import unittest
import jsonpointer
import jsonpatch
from random import randint as rn, choice as ch


def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(filename, file)


data = {
    "1": {"record_id": 1, "foo": "foo", "bar": "bar"},
    "2": {"record_id": 2, "foo": "fizz", "bar": "buzz"}
}

write(data, 'data.json')


def json_data():
    scr = {"1": {"foo": "foo", "bar": "bar"}}
    drt = {"2": {"foo": "fizz", "bar": "buzz"}}
    patch = jsonpatch.make_patch(scr, drt)
