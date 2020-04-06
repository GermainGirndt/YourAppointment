import unittest
from unittest import mock
from ClassesManager import ClassesManager as erp
import sys
from io import StringIO

class test_AddStudent(unittest.TestCase):

	rightInputs1 = ["João", "da Silva", "23-05-1978", "297.586.890-10", "Bom Sucesso, 487", "Casa", "São Paulo", "SP"]
	
	rightInputs2 = ["Joana", "Silveira", "17-02-1972", "434.763.780-20", "Felicidade, 14", "Ap. 201", "Rio de Janeiro", "RJ"]

	def setUp(self):
		self.erp_Instance = erp()


	def test_add1Student_pass(self):
		with mock.patch('ClassesManager.input', side_effect=self.rightInputs1):
			self.erp_Instance.addStudent()
		self.assertEqual(self.erp_Instance.students[0], self.rightInputs1)


	def test_add2Students_pass(self):

		with mock.patch('ClassesManager.input', side_effect=self.rightInputs2):
			self.erp_Instance.addStudent()
		self.assertEqual(self.erp_Instance.students[0], self.rightInputs2)


		with mock.patch('ClassesManager.input', side_effect=self.rightInputs1):
			self.erp_Instance.addStudent()
		self.assertEqual(self.erp_Instance.students[1], self.rightInputs1)


		self.assertEqual(self.erp_Instance.students, [self.rightInputs2, self.rightInputs1])



	def test_add1Student_fails_numbersInString(self):
		wrongInput = "João2"
		inputedInputs = [wrongInput, "João", "da Silva", "23-05-1978", "297.586.890-10", "Bom Sucesso, 487", "Casa", "São Paulo", "SP"]
		exceptionEsperada = "Invalid input. The name muss contain only letter or spaces."
		self.held, sys.stdout = sys.stdout, StringIO()
		with mock.patch('ClassesManager.input', side_effect=inputedInputs):
			self.erp_Instance.addStudent()
		self.assertEqual(self.erp_Instance.students[-1], self.rightInputs1)
		mensagensPrintadas = sys.stdout.getvalue()
		self.assertIn(exceptionEsperada, mensagensPrintadas)
		self.held, sys.stdout = None, None


	def test_add1Student_fails_TypeError(self):
		wrongInput = 2
		inputedInputs = [wrongInput, "João", "da Silva", "23-05-1978", "297.586.890-10", "Bom Sucesso, 487", "Casa", "São Paulo", "SP"]
		with mock.patch('ClassesManager.input', side_effect=inputedInputs):
			self.assertRaises(TypeError, lambda x:self.erp_Instance.addStudent())


	def tearDown(self):
		self.erp_Instance = "la"
	


class test_RemoveStudent(unittest.TestCase):
	pass


class test_showStudents(unittest.TestCase):
	pass


class test_showClassSchedule(unittest.TestCase):
	pass

class test_addClassSchedule(unittest.TestCase):
	pass

class test_removeSchedule(unittest.TestCase):
	pass

class test_addClass(unittest.TestCase):
	pass

class test_setNotification(unittest.TestCase):
	pass

class test_setAllNtoification(unittest.TestCase):
	pass

if __name__ == "__main__":
	unittest.main()
