import unittest
import logging
logger = logging.getLogger(__name__)
class LogTest(unittest.TestCase):
    def test_log_print(self):
        logging.debug("This is debug error")
        logging.info("This is Info error")
        logging.warning("This is warning ")
        logging.error("This is error")


if __name__ == '__main__':
    unittest.main()