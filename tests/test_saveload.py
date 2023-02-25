import unittest

import aergia
import os


def create_temp_folder():
    # create a temporary folder for file creation
    path = "/temp"

    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)


def delete_temp_folder():
    path = "/temp"
    try:
        os.rmdir(path)
    except OSError:
        print("Deletion of the directory %s failed" % path)
    else:
        print("Successfully deleted the directory %s" % path)


def test_init():
    create_temp_folder()
    file_dict = {"save1": "save1.json",
                 "save2": "save2.json"}
    s = aergia.SaveLoadSystem("temp/", file_dict)
    return s


class SaveLoadTest(unittest.TestCase):
    def file_creation(self):
        """Test file are properly created"""
        # create a tem
        create_temp_folder()
        file_dict = {"save1": "save1.json",
                     "save2": "save2.json"}
        s = aergia.SaveLoadSystem("temp/", file_dict)

        s1 = s.get_path("save1")
        result = "temp/save1.json"
        self.assertEqual(s1, result)


if __name__ == '__main__':
    unittest.main()
