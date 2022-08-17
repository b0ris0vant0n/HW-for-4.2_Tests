import unittest
from main import create_folder, get_folder_type

folder_name = 'TEST'
class TestFunctions(unittest.TestCase):

    def test_create_dir(self):
        self.assertEqual(create_folder(folder_name), 201)

    def test_get_info(self):
        self.assertTrue(get_folder_type(folder_name) == 'dir')

    def test_create_dir(self):
        self.assertEqual(create_folder(folder_name), 409)

