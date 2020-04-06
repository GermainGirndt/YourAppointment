import unittest
from unittest import mock
from ClassesManager import ClassesManager as erp
import sys
from io import StringIO

class test_AddStudent(unittest.TestCase):

	rightInputs_StudentId0 = ["João", "da Silva", "23-05-1978", "297.586.890-10", "Bom Sucesso, 487", "Casa", "São Paulo", "SP"]
	
	rightInputs_StudentId1 = ["Joana", "Silveira", "17-02-1972", "434.763.780-20", "Felicidade, 14", "Ap. 201", "Rio de Janeiro", "RJ"]

	def setUp(self):
		self.erp_Instance = erp()


	def test_add1Student_passes(self):
		with mock.patch('ClassesManager.input', side_effect=self.rightInputs_StudentId0):
			self.erp_Instance.addStudent()
		self.assertEqual(self.erp_Instance.students[0], self.rightInputs_StudentId0)


	def test_add2Students_passes(self):

		with mock.patch('ClassesManager.input', side_effect=self.rightInputs_StudentId1):
			self.erp_Instance.addStudent()
		self.assertEqual(self.erp_Instance.students[0], self.rightInputs_StudentId1)


		with mock.patch('ClassesManager.input', side_effect=self.rightInputs_StudentId0):
			self.erp_Instance.addStudent()
		self.assertEqual(self.erp_Instance.students[1], self.rightInputs_StudentId0)


		self.assertEqual(self.erp_Instance.students, [self.rightInputs_StudentId1, self.rightInputs_StudentId0])



	def test_add1Student_fails_numbersInString(self):
		wrongInput = "João2"
		inputedInputs = [wrongInput, "João", "da Silva", "23-05-1978", "297.586.890-10", "Bom Sucesso, 487", "Casa", "São Paulo", "SP"]
		exceptionEsperada = "Invalid input. The name muss contain only letter or spaces."
		self.held, sys.stdout = sys.stdout, StringIO()
		with mock.patch('ClassesManager.input', side_effect=inputedInputs):
			self.erp_Instance.addStudent()
		self.assertEqual(self.erp_Instance.students[-1], self.rightInputs_StudentId0)
		mensagensPrintadas = sys.stdout.getvalue()
		self.assertIn(exceptionEsperada, mensagensPrintadas)
		self.held, sys.stdout = None, None


	def test_add1Student_fails_TypeError(self):
		wrongInput = 2
		inputedInputs = [wrongInput, "João", "da Silva", "23-05-1978", "297.586.890-10", "Bom Sucesso, 487", "Casa", "São Paulo", "SP"]
		with mock.patch('ClassesManager.input', side_effect=inputedInputs):
			self.assertRaises(TypeError, lambda x:self.erp_Instance.addStudent())


	def tearDown(self):
		self.erp_Instance = None
	




class test_RemoveStudentById(unittest.TestCase):

	def setUp(self):
		self.erp_Instance = erp()
		self.rightInputs_StudentId0 = ["João", "da Silva", "23-05-1978", "297.586.890-10", "Bom Sucesso, 487", "Casa", "São Paulo", "SP"]
		self.rightInputs_StudentId1 = ["Joana", "Silveira", "17-02-1972", "434.763.780-20", "Felicidade, 14", "Ap. 201", "Rio de Janeiro", "RJ"]
		with mock.patch('ClassesManager.input', side_effect=self.rightInputs_StudentId0):
			self.erp_Instance.addStudent()
		with mock.patch('ClassesManager.input', side_effect=self.rightInputs_StudentId1):
			self.erp_Instance.addStudent()
		self.assertEqual(len(self.erp_Instance.students), 2) #Checks
		self.assertIn(self.rightInputs_StudentId0, self.erp_Instance.students)
		self.assertIn(self.rightInputs_StudentId1, self.erp_Instance.students)


	def test_remove1StudentById_passes(self):
		rightId = ["0"]
		with mock.patch('ClassesManager.input', side_effect=rightId):
			self.erp_Instance.removeStudentById()
		self.assertEqual(len(self.erp_Instance.students), 1)
		self.assertNotIn(self.rightInputs_StudentId0, self.erp_Instance.students)

	def test_remove1StudentById_passes2(self):
		rightId = ["1"]
		with mock.patch('ClassesManager.input', side_effect=rightId):
			self.erp_Instance.removeStudentById()
		self.assertEqual(len(self.erp_Instance.students), 1)
		self.assertNotIn(self.rightInputs_StudentId1, self.erp_Instance.students)

	def test_remove1StudentById_fails_InexistingId(self):
		wrongInput_id = "200"
		rightInput_id = "0"
		inputedInputs = [wrongInput_id, rightInput_id]
		exceptionEsperada = f"The inputed value is out of range. Please input a index from 0 to {len(self.erp_Instance.students)}"
		self.held, sys.stdout = sys.stdout, StringIO()
		with mock.patch('ClassesManager.input', side_effect=inputedInputs):
			self.erp_Instance.removeStudentById()
		mensagensPrintadas = sys.stdout.getvalue()
		self.assertIn(exceptionEsperada, mensagensPrintadas)
		self.assertEqual(len(self.erp_Instance.students), 1)
		self.assertNotIn(self.rightInputs_StudentId0, self.erp_Instance.students)
		self.held, sys.stdout = None, None




	def test_remove1StudentById_fails_ValueError(self):
		wrongInput = ["lala"]
		with mock.patch('ClassesManager.input', side_effect=wrongInput):
			self.assertRaises(ValueError, lambda: self.erp_Instance.removeStudentById())
		self.assertEqual(len(self.erp_Instance.students), 2)
		self.assertIn(self.rightInputs_StudentId0, self.erp_Instance.students)
		self.assertIn(self.rightInputs_StudentId1, self.erp_Instance.students)

	def tearDown(self):
		self.erp_Instance = None




class test_RemoveStudentByName(unittest.TestCase):

	def setUp(self):
		self.erp_Instance = erp()
		rightInputs_StudentId0 = ["João", "da Silva", "23-05-1978", "297.586.890-10", "Bom Sucesso, 487", "Casa", "São Paulo", "SP"]
		rightInputs_StudentId1 = ["Joana", "Silveira", "17-02-1972", "434.763.780-20", "Felicidade, 14", "Ap. 201", "Rio de Janeiro", "RJ"]
		with mock.patch('ClassesManager.input', side_effect=rightInputs_StudentId0):
			self.erp_Instance.addStudent()
		with mock.patch('ClassesManager.input', side_effect=rightInputs_StudentId1):
			self.erp_Instance.addStudent()


	def test_remove1StudentByName_passes(self):
		self.assertEqual(len(self.erp_Instance.students), 2) 
		self.assertEqual(self.erp_Instance.removeStudentByName(), 1)



	def tearDown(self):
		self.erp_Instance = None



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
