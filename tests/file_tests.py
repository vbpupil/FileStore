import unittest
from File import File

class FileTest(unittest.TestCase):
    f = None

    def setUp(self):
        self.f=File()
        self.f.set_file('test.txt')

    def testGetFile(self):
        self.assertEqual('test.txt', self.f.get_file())
