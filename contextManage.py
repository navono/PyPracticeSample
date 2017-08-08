import json

data = """{
    "name": "JSON",
    "details": {
        "extension": ".json",
        "type": "TEXT",
        "format": "Data-Interchange",
        "standartd": "RFC 7159"
    },
    "website": "json.org"
}"""


class OpenJSONFile():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.json_file = open(self.filename, self.mode)
        return self.json_file

    def __exit__(self, type, value, traceback):
        self.json_file.close()


def write_to_json_file(filename, data):
    # with open(filename, 'wt') as json_file:
    with OpenJSONFile(filename=filename, mode='wt') as json_file:
        json_data = json.loads(data)
        json.dump(json_data, json_file)


write_to_json_file('the_json_file.json', data)
