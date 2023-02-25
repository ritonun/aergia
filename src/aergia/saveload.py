import json


class SaveLoadSystem:
    def __init__(self, save_folder, files_dict):
        self.save_folder = save_folder
        self.files = files_dict
        self.create_files()

    def get_path(self, file_key):
        return self.save_folder + self.files[file_key]

    def create_files(self):
        for file_key in self.files:
            try:
                f = open(self.save_folder + self.files[file_key], "r")
                f.close()
            except FileNotFoundError:
                f = open(self.save_folder + self.files[file_key], "x")
                f.close()

    def load_file(self, file_key):
        data = None
        with open(self.get_path(file_key), "r") as f:
            data = json.load(f)
        return data

    def save_data(self, file_key, data: dict):
        with open(self.get_path(file_key), "w") as f:
            json.dump(data, f, indent=2)

    def optimize_json(self):
        pass

    def optimized_save(self, file_key, data):
        pass
