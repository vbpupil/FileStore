import unittest
from filestore.File import File

class FileTest(unittest.TestCase):
    f = None

    def setUp(self):
        self.f=File()
        self.f.set_file('ttt.txt')

    def testGetFile(self):
        self.assertEqual('ttt.txt', self.f.get_file())
