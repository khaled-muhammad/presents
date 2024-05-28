import json

class BookScheme:
    def __init__(self, data:dict):
        self.data = data
        self.name = data['doc_name']
        self.path = data['path']
        self.excluded_files_names = data['excluded_files_names']

    def get_files_priority(self):
        return self.data.get("files_periority", [])

    def get_extended_file_name(self, key):
        extended_files_names = self.data.get("extended_files_names", {})
        return extended_files_names.get(key, None)

    def is_excluded(self, file_name):
        return file_name in self.excluded_files_names

    def get_test_scheme(self):
        return self.data.get("test_scheme", [])

    def get_test_titles(self):
        return self.data.get("test_titles", [])

    def get_marginalia(self):
        return self.data.get("marginalia", None)

    def __str__(self):
        return f'Name: {self.name}\nPath: {self.path}'

    @staticmethod
    def from_json_file(file_path):
        with open(file_path, "r") as file:
            json_data = json.load(file)

        return BookScheme(json_data)

