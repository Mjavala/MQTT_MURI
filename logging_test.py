import unittest
import muri_logging


class TestBuildDir(unittest.TestCase):

    def test_build_dir(self):
        result = muri_logging.build_dir('M', 'test')
        self.assertEqual(result, 'C:/Users/jose/Projects/muri/logs/hourly/test')


class TestLogObj(unittest.TestCase):

    message = {
        
    }

    def test_log_ob(self):
        result = muri_logging.log_obj('H','test', messsage)
        with self.assertLogs('logger', level='INFO') as cm:
            logging.getLogger('logger').info('first message')


if __name__ == "__main__":
    unittest.main()