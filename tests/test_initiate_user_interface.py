import set_test_path
import unittest
from unittest import mock
from io import StringIO
from contextlib import redirect_stdout
from app import ConsoleUI



class TestUserInterface(unittest.TestCase):

    def setUp(self):
        self.console_ui = ConsoleUI()


if __name__ == "__main__":
    unittest.main()