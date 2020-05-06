import set_test_path
import unittest
from data_manager import DataManager
from data_manager import Database
import sqlite3
import os
from datetime import datetime
from unittest import mock
from testing_resources import TestingShortcuts

class test_add_customer_to_database(unittest.TestCase, TestingShortcuts):

    def setUp(self):
        db_file = "YourAppointment.db"
        if os.path.exists(db_file):
            os.remove(db_file)

    def test_add_1_customer_to_database(self):
        self.dm = DataManager()
        with mock.patch('builtins.input', side_effect=self.RIGHT_INPUTS_CUSTOMER_ID_1):
            self.dm.add_new_customer_to_database()
        self.assertEqual(self.DB_RIGHT_RETURN_CUSTOMER_ID_1, self.dm.fetchone())


if __name__ == "__main__":
    unittest.main()