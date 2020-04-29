import set_test_path
import unittest
from app import AppointmentsManagementSystem as Ams
import sqlite3

class test_add_customer_to_database(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect('YourAppointment.db')
        self.c = self.conn.cursor()

    def test_add_1_customer_to_datebase(self):
        self.ams_instance = Ams()
        self.ams_instance.add_new_customer_to_database()
        self.c.execute("SELECT * FROM customers")
        self.assertEqual(self.c.fetchone(), ("João", "da Silva", "23-05-1978", "297.586.890-10", "Rua Bom Sucesso, 487", "Casa",
                                 "São Paulo", "SP"))

    def tearDown(self):
        self.conn.close()

if __name__ == "__main__":
    unittest.main()