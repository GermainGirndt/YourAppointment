import sys
from io import StringIO
import unittest
from unittest import mock
import set_test_path
from app import ClassesManagementSystem as Erp


class test_remove_student_by_index(unittest.TestCase):

	def setUp(self):
		self.erp_instance = Erp()
		self.right_inputs_student_id_0 = ["João", "da Silva", "23-05-1978", "297.586.890-10", "Rua Bom Sucesso, 487", "Casa", "São Paulo", "SP"]
		self.right_inputs_student_id_1 = ["Joana", "Silveira", "17-02-1972", "434.763.780-20", "Felicidade, 14", "Ap. 201", "Rio de Janeiro", "RJ"]
		with mock.patch('builtins.input', side_effect=self.right_inputs_student_id_0):
			self.erp_instance.add_student()
		with mock.patch('builtins.input', side_effect=self.right_inputs_student_id_1):
			self.erp_instance.add_student()
		self.assertEqual(len(self.erp_instance.students), 2) #Checks
		self.assertIn(self.right_inputs_student_id_0, self.erp_instance.students)
		self.assertIn(self.right_inputs_student_id_1, self.erp_instance.students)

	def test_remove_1_student_by_index_passes(self):
		rightId = "0"
		with mock.patch('builtins.input', side_effect=rightId):
			self.erp_instance.remove_student_by_index()
		self.assertEqual(len(self.erp_instance.students),1)
		self.assertNotIn(self.right_inputs_student_id_0, self.erp_instance.students)

	def test_remove_1_student_by_index_passes2(self):
		rightId = ["1"]
		with mock.patch('builtins.input', side_effect=rightId):
			self.erp_instance.remove_student_by_index()
		self.assertEqual(len(self.erp_instance.students), 1)
		self.assertNotIn(self.right_inputs_student_id_1, self.erp_instance.students)


	def test_remove_1_student_by_index_fails_inexisting_index(self):
		wrong_input_id = "200"
		right_input_id = "0"
		inputed_inputs = [wrong_input_id, right_input_id]
		expected_exception = f"The inputed value is out of range. Please input a index from 0 to {len(self.erp_instance.students)}"
		self.held, sys.stdout = sys.stdout, StringIO()
		with mock.patch('builtins.input', side_effect=inputed_inputs):
			self.erp_instance.remove_student_by_index()
		printed_messages = sys.stdout.getvalue()
		self.assertIn(expected_exception, printed_messages)
		self.assertEqual(len(self.erp_instance.students), 1)
		self.assertNotIn(self.right_inputs_student_id_0, self.erp_instance.students)
		self.held = None #removed 'sys.stdout = None' due to issues with pycharm

	def test_remove_1_student_by_index_fails_type_error(self):
		wrong_input = [5]
		with mock.patch('builtins.input', side_effect=wrong_input):
			with self.assertRaises(TypeError):
				self.erp_instance.remove_student_by_index()
		self.assertEqual(len(self.erp_instance.students), 2)
		self.assertIn(self.right_inputs_student_id_0, self.erp_instance.students)
		self.assertIn(self.right_inputs_student_id_1, self.erp_instance.students)

	def test_remove_1_student_by_index_fails_value_error(self):
		wrong_input = ["lala"]
		with mock.patch('builtins.input', side_effect=wrong_input):
			with self.assertRaises(ValueError):
				self.erp_instance.remove_student_by_index()
		self.assertEqual(len(self.erp_instance.students), 2)
		self.assertIn(self.right_inputs_student_id_0, self.erp_instance.students)
		self.assertIn(self.right_inputs_student_id_1, self.erp_instance.students)

	def tearDown(self):
		self.erp_instance = None

if __name__ == "__main__":
	unittest.main()