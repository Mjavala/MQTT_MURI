import unittest
import muri_logging


class TestBuildDir(unittest.TestCase):

    def test_build_dir(self):
        result = muri_logging.build_dir('test')
        self.assertEqual(result, 'C:/Users/jose/Projects/muri/logs/hourly/test')


if __name__ == "__main__":
    unittest.main()