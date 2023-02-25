import pytest
from aergia import SaveLoadSystem
import os


def create_temp_folder():
    # create a temporary folder for file creation
    path = "temp/"

    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)


def delete_temp_folder():
    path = "temp"
    try:
        os.rmdir(path)
    except OSError:
        print("Deletion of the directory %s failed" % path)
    else:
        print("Successfully deleted the directory %s" % path)


class TestSaveLoadSystem:
    def test_file_creation(self):
        """Test file are properly created"""
        # create a tem
        create_temp_folder()
        file_dict = {"save1": "save1.json",
                     "save2": "save2.json"}
        s = SaveLoadSystem("temp/", file_dict)
        delete_temp_folder()
        s1 = s.get_path("save1")
        result = "temp/save1.json"
        assert s1 == result

    def test_save_and_load(self):
        create_temp_folder()
        file_dict = {"save1": "save1.json", "save2": "save2.json"}
        s = SaveLoadSystem("temp/", file_dict)
        data = {"var": 1.0}
        s.save_data("save1", data)
        loaded_data = s.load_file("save1")
        delete_temp_folder()
        assert loaded_data["var"] == 1.0
