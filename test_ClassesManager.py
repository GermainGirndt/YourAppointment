import unittest
from unittest import mock
import os
from ClassesManager import ClassesManager as erp

class test_AddStudent(unittest.TestCase):

	def setUp(self):
		self.erp_Instance = erp()

	def test_addStudent_correct(self):
		inputs = ["Germain", "Martins Pereira", "25-03-2020", "016.206.476-48", "Dois de Julho, 229", "casa", "Governador Valadares", "MG"]
		with mock.patch('ClassesManager.input', side_effect=inputs):
			self.erp_Instance.addStudent()
		self.assertEqual(self.erp_Instance.students[-1], inputs)
		

	def test_addStudent_incorrect_numbers(self):
		wrongInput = "João2"
		rightInputs = ["João", "da Silva", "23-05-1978", "297.586.890-10", "Bom Sucesso, 487", "Casa", "São Paulo", "SP"]
		inputedInputs = [wrongInput, "João", "da Silva", "23-05-1978", "297.586.890-10", "Bom Sucesso, 487", "Casa", "São Paulo", "SP"]
		with mock.patch('ClassesManager.input', side_effect=inputedInputs):
			self.erp_Instance.addStudent()
		self.assertEqual(self.erp_Instance.students[-1], rightInputs)


		resultadoErrado = "1"
		exceptionEsperada = "Entrada inválida. A razão social só deve conter letras e espaços."
		self.held, sys.stdout = sys.stdout, StringIO()
		with mock.patch('ProjetoFinalDeploy.input', side_effect=[resultadoErrado, self.resultadoCorreto]):
			self.assertEqual(pf.empresa_CadastrarRazaoSocial(), self.resultadoCorreto)
		mensagensPrintadas = sys.stdout.getvalue()
		self.assertIn(exceptionEsperada, mensagensPrintadas)
		self.held, sys.stdout = None, None



		def tearDown(self):
			self.erp_Instance = None


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

class test_setAllNotification(unittest.TestCase):
	pass

if __name__ == "__main__":
	unittest.main()
