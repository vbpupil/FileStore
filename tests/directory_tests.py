import unittest
from directory.Directory import Directory


class DirectoryTest(unittest.TestCase):
    d = None

    def setUp(self):
        # super(DirectoryTest, self).setUp()
        self.d = Directory()

    def test_get_path(self):
        self.d.set_path('/home/dean/tmp/')
        self.assertEqual('/home/dean/tmp/', self.d.get_path())

    def test_get_path_exception(self):
        with self.assertRaises(Exception, msg="Directory has not been set."):
            self.d.get_path()


if __name__ == '__main__': unittest.main()
