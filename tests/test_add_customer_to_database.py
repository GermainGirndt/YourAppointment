import set_test_path
import unittest
from app import AppointmentsManagementSystem as Ams
import sqlite3
import os
from datetime import datetime
from unittest import mock


class test_add_customer_to_database(unittest.TestCase):

    customer_register_day = datetime.now().strftime("%Y-%m-%d")
    customer_register_time = datetime.now().strftime("%H:%M:%S")

    RIGHT_INPUTS_CUSTOMER_ID_0 = ("João", "da Silva", "23-05-1978", "297.586.890-10",
                                  "Rua Bom Sucesso, 487", "Casa", "São Paulo",
                                  "SP", customer_register_day, customer_register_time, "Active")

    RIGHT_INPUTS_CUSTOMER_ID_1 = ("Joana", "Silveira", "17-02-1972", "434.763.780-20", "Felicidade, 14", "Ap. 201",
                                  "Rio de Janeiro", "RJ", customer_register_day, customer_register_time, "Active")

    def setUp(self):
        self.conn = sqlite3.connect('YourAppointment.db')
        self.c = self.conn.cursor()

    def test_add_1_customer_to_database(self):
        self.ams_instance = Ams()
        with mock.patch('builtins.input', side_effect=self.RIGHT_INPUTS_CUSTOMER_ID_0):
            self.ams_instance.add_new_customer_to_database()
            self.c.execute("SELECT * FROM customers")
        self.assertEqual(self.c.fetchone(), self.RIGHT_INPUTS_CUSTOMER_ID_0)

    def tearDown(self):
        self.conn.close()
        self.ams_instance = None
        os.remove("YourAppointment.db")


if __name__ == "__main__":
    unittest.main()