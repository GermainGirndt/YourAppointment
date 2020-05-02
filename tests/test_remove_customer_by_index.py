import set_test_path
import unittest
from unittest import mock
from io import StringIO
from contextlib import redirect_stdout
from app import AppointmentManagementSystem as Ams
from datetime import datetime

class test_remove_customer_by_index(unittest.TestCase):

	def setUp(self):
		customer_register_day = datetime.now().strftime("%Y-%m-%d")
		customer_register_time = datetime.now().strftime("%H:%M")

		self.RIGHT_INPUTS_CUSTOMER_ID_1 = ["João", "da Silva", "23-05-1978",
									  "297.586.890-10", "Rua Bom Sucesso, 487",
									  "Casa", "São Paulo", "SP"]

		self.RIGHT_RETURN_CUSTOMER_ID_1 = ["João", "da Silva", "1978-05-23",
									  "297.586.890-10", "Rua Bom Sucesso, 487",
									  "Casa", "São Paulo", "SP",
									  customer_register_day, customer_register_time, "Active"]

		self.RIGHT_INPUTS_CUSTOMER_ID_2 = ["Joana", "Silveira", "17-02-1972",
									  "434.763.780-20", "Felicidade, 14", "Ap. 201",
									  "Rio de Janeiro", "RJ"]

		self.RIGHT_RETURN_CUSTOMER_ID_2 = ["Joana", "Silveira", "1972-02-17",
									  "434.763.780-20", "Felicidade, 14", "Ap. 201",
									  "Rio de Janeiro", "RJ",
									  customer_register_day, customer_register_time, "Active"]

		self.ams_instance = Ams()
		with mock.patch('builtins.input', side_effect=self.RIGHT_INPUTS_CUSTOMER_ID_1):
			self.ams_instance.add_customer_to_registry()
		with mock.patch('builtins.input', side_effect=self.RIGHT_INPUTS_CUSTOMER_ID_2):
			self.ams_instance.add_customer_to_registry()
		self.assertEqual(len(self.ams_instance.customers_registry), 2) #Checks
		self.assertIn(self.RIGHT_RETURN_CUSTOMER_ID_1, self.ams_instance.customers_registry)
		self.assertIn(self.RIGHT_RETURN_CUSTOMER_ID_2, self.ams_instance.customers_registry)

	def test_remove_1_customer_by_index_passes(self):
		rightId = "1"
		with mock.patch('builtins.input', side_effect=rightId):
			self.ams_instance.remove_customer_by_index()
		self.assertEqual(1, len(self.ams_instance.customers_registry))
		self.assertNotIn(self.RIGHT_RETURN_CUSTOMER_ID_1, self.ams_instance.customers_registry)

	def test_remove_1_customer_by_index_passes2(self):
		rightId = ["2"]
		with mock.patch('builtins.input', side_effect=rightId):
			self.ams_instance.remove_customer_by_index()
		self.assertEqual(1, len(self.ams_instance.customers_registry))
		self.assertNotIn(self.RIGHT_RETURN_CUSTOMER_ID_2, self.ams_instance.customers_registry)


	def test_remove_1_customer_by_index_fails_inexisting_index(self):
		wrong_input_id = "200"
		right_input_id = "1"
		inputed_inputs = [wrong_input_id, right_input_id]
		expected_exception = f"Invalid input. The id of the customer to be removed " \
							 f"muss be between 1 and {len(self.ams_instance.customers_registry)}"
		with redirect_stdout(StringIO()) as stdout:
			with mock.patch('builtins.input', side_effect=inputed_inputs):
				self.ams_instance.remove_customer_by_index()
		printed_messages = stdout.getvalue()
		self.assertIn(expected_exception, printed_messages)
		self.assertEqual(len(self.ams_instance.customers_registry), 1)
		self.assertNotIn(self.RIGHT_RETURN_CUSTOMER_ID_1, self.ams_instance.customers_registry)


	def test_remove_1_customer_by_index_fails_type_error(self):
		wrong_input = [5]
		with mock.patch('builtins.input', side_effect=wrong_input):
			with self.assertRaises(TypeError):
				self.ams_instance.remove_customer_by_index()
		self.assertEqual(len(self.ams_instance.customers_registry), 2)
		self.assertIn(self.RIGHT_RETURN_CUSTOMER_ID_1, self.ams_instance.customers_registry)
		self.assertIn(self.RIGHT_RETURN_CUSTOMER_ID_2, self.ams_instance.customers_registry)

	def test_remove_1_customer_by_index_fails_value_error(self):
		wrong_input_id = "lalala"
		right_input_id = "1"
		inputed_inputs = [wrong_input_id, right_input_id]
		expected_exception = f"Invalid input. The id of the customer to be removed " \
							 f"muss be a number"
		with redirect_stdout(StringIO()) as stdout:
			with mock.patch('builtins.input', side_effect=inputed_inputs):
				self.ams_instance.remove_customer_by_index()
		printed_messages = stdout.getvalue()
		self.assertIn(expected_exception, printed_messages)
		self.assertEqual(len(self.ams_instance.customers_registry), 1)
		self.assertNotIn(self.RIGHT_RETURN_CUSTOMER_ID_1, self.ams_instance.customers_registry)

	def test_remove_2_customers_by_index_passes(self):
		rightId = ["1","2"]
		with mock.patch('builtins.input', side_effect=rightId):
			self.ams_instance.remove_customer_by_index()
		self.assertEqual(1, len(self.ams_instance.customers_registry))
		self.assertNotIn(self.RIGHT_RETURN_CUSTOMER_ID_1, self.ams_instance.customers_registry)


	def tearDown(self):
		self.ams_instance = None

if __name__ == "__main__":
	unittest.main()