import set_test_path
import unittest
from data_manager import DataManager
from data_manager import Database
import sqlite3
import os
from datetime import datetime
from unittest import mock
from testing_resources import TestingShortcuts
from contextlib import redirect_stdout
from io import StringIO

class test_add_new_customer_to_database(unittest.TestCase,TestingShortcuts):

    def setUp(self):
        db_file = "YourAppointment.db"
        if os.path.exists(db_file):
            os.remove(db_file)
        self.dm = DataManager()
        with redirect_stdout(StringIO()) as stdout:
            self.dm.db.create_table_customers()


    def test_add_customer_id_1_to_database(self):
        self.shortcut_add_customer_to_datebase(
            self.RIGHT_INPUTS_CUSTOMER_ID_1, self.DB_RIGHT_RETURN_CUSTOMER_ID_1
        )

    def test_add_customer_id_1_and_2_to_database(self):
        self.test_add_customer_id_1_to_database()
        self.shortcut_add_customer_to_datebase(
            self.RIGHT_INPUTS_CUSTOMER_ID_2, self.DB_RIGHT_RETURN_CUSTOMER_ID_2
        )





if __name__ == "__main__":
    unittest.main()