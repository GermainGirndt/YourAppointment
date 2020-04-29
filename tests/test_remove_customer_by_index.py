import set_test_path
import unittest
from unittest import mock
from io import StringIO
from contextlib import redirect_stdout
from app import AppointmentsManagementSystem as Ams
from datetime import datetime

class test_remove_customer_by_index(unittest.TestCase):

	def setUp(self):
		customer_register_day = datetime.now().strftime("%Y-%m-%d")
		customer_register_time = datetime.now().strftime("%H:%M")

		self.ams_instance = Ams()
		self.right_inputs_customer_id_0 = ["João", "da Silva", "23-05-1978", "297.586.890-10", "Rua Bom Sucesso, 487", "Casa", "São Paulo", "SP", customer_register_day, customer_register_time, "Active"]
		self.right_inputs_customer_id_1 = ["Joana", "Silveira", "17-02-1972", "434.763.780-20", "Felicidade, 14", "Ap. 201", "Rio de Janeiro", "RJ", customer_register_day, customer_register_time, "Active"]

		with mock.patch('builtins.input', side_effect=self.right_inputs_customer_id_0):
			self.ams_instance.add_customer_to_registry()
		with mock.patch('builtins.input', side_effect=self.right_inputs_customer_id_1):
			self.ams_instance.add_customer_to_registry()
		self.assertEqual(len(self.ams_instance.customers_register), 2) #Checks
		self.assertIn(self.right_inputs_customer_id_0, self.ams_instance.customers_register)
		self.assertIn(self.right_inputs_customer_id_1, self.ams_instance.customers_register)

	def test_remove_1_customer_by_index_passes(self):
		rightId = "0"
		with mock.patch('builtins.input', side_effect=rightId):
			self.ams_instance.remove_customer_by_index()
		self.assertEqual(len(self.ams_instance.customers_register),1)
		self.assertNotIn(self.right_inputs_customer_id_0, self.ams_instance.customers_register)

	def test_remove_1_customer_by_index_passes2(self):
		rightId = ["1"]
		with mock.patch('builtins.input', side_effect=rightId):
			self.ams_instance.remove_customer_by_index()
		self.assertEqual(len(self.ams_instance.customers_register), 1)
		self.assertNotIn(self.right_inputs_customer_id_1, self.ams_instance.customers_register)


	def test_remove_1_customer_by_index_fails_inexisting_index(self):
		wrong_input_id = "200"
		right_input_id = "0"
		inputed_inputs = [wrong_input_id, right_input_id]
		expected_exception = f"The inputed value is out of range. Please input a index from 0 to {len(self.ams_instance.customers_register)}"
		with redirect_stdout(StringIO()) as stdout:
			with mock.patch('builtins.input', side_effect=inputed_inputs):
				self.ams_instance.remove_customer_by_index()
		printed_messages = stdout.getvalue()
		self.assertIn(expected_exception, printed_messages)
		self.assertEqual(len(self.ams_instance.customers_register), 1)
		self.assertNotIn(self.right_inputs_customer_id_0, self.ams_instance.customers_register)


	def test_remove_1_customer_by_index_fails_type_error(self):
		wrong_input = [5]
		with mock.patch('builtins.input', side_effect=wrong_input):
			with self.assertRaises(TypeError):
				self.ams_instance.remove_customer_by_index()
		self.assertEqual(len(self.ams_instance.customers_register), 2)
		self.assertIn(self.right_inputs_customer_id_0, self.ams_instance.customers_register)
		self.assertIn(self.right_inputs_customer_id_1, self.ams_instance.customers_register)

	def test_remove_1_customer_by_index_fails_value_error(self):
		wrong_input = ["lala"]
		with mock.patch('builtins.input', side_effect=wrong_input):
			with self.assertRaises(ValueError):
				self.ams_instance.remove_customer_by_index()
		self.assertEqual(len(self.ams_instance.customers_register), 2)
		self.assertIn(self.right_inputs_customer_id_0, self.ams_instance.customers_register)
		self.assertIn(self.right_inputs_customer_id_1, self.ams_instance.customers_register)

	def test_remove_2_customers_by_index_passes(self):
		rightId = ["0","1"]
		with mock.patch('builtins.input', side_effect=rightId):
			self.ams_instance.remove_customer_by_index()
		self.assertEqual(len(self.ams_instance.customers_register),1)
		self.assertNotIn(self.right_inputs_customer_id_0, self.ams_instance.customers_register)


	def tearDown(self):
		self.ams_instance = None

if __name__ == "__main__":
	unittest.main()