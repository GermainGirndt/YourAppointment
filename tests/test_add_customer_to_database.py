import set_test_path
import unittest
from app import AppointmentManagementSystem
from app import Database
import sqlite3
import os
from datetime import datetime
from unittest import mock


class test_add_customer_to_database(unittest.TestCase):

    customer_register_day = datetime.now().strftime("%Y-%m-%d")
    customer_register_time = datetime.now().strftime("%H:%M")

    RIGHT_INPUTS_CUSTOMER_ID_1 = ("João", "da Silva", "23-05-1978", "297.586.890-10",
                                  "Rua Bom Sucesso, 487", "Casa", "São Paulo",
                                  "SP", customer_register_day, customer_register_time, "Active")

    RIGHT_RETURN_CUSTOMER_ID_1 = (1, "João", "da Silva", "1978-05-23", "297.586.890-10",
                                  "Rua Bom Sucesso, 487", "Casa", "São Paulo",
                                  "SP", customer_register_day, customer_register_time, "Active")

    RIGHT_INPUTS_CUSTOMER_ID_2 = ("Joana", "Silveira", "17-02-1972", "434.763.780-20", "Felicidade, 14", "Ap. 201",
                                  "Rio de Janeiro", "RJ", customer_register_day, customer_register_time, "Active")

    RIGHT_RETURN_CUSTOMER_ID_2 = (2, "Joana", "Silveira", "1972-02-17", "434.763.780-20", "Felicidade, 14", "Ap. 201",
                                  "Rio de Janeiro", "RJ", customer_register_day, customer_register_time, "Active")


    def setUp(self):
        db_file = "YourAppointment.db"
        if os.path.exists(db_file):
            os.remove(db_file)

    def test_add_1_customer_to_database(self):
        self.ams = AppointmentManagementSystem()
        with mock.patch('builtins.input', side_effect=self.RIGHT_INPUTS_CUSTOMER_ID_1):
            self.ams.add_new_customer_to_database()
        self.assertEqual(self.RIGHT_RETURN_CUSTOMER_ID_1, self.ams.fetchone())


if __name__ == "__main__":
    unittest.main()