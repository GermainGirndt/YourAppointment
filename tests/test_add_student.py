import sys
sys.path.append("..") #Enables the relative import
from io import StringIO
import unittest
from unittest import mock
from main_ClassesManagementSystem import ClassesManagementSystem as Erp


class test_add_student(unittest.TestCase):
    right_inputs_student_id_0 = ["João", "da Silva", "23-05-1978", "297.586.890-10", "Rua Bom Sucesso, 487", "Casa",
                                 "São Paulo", "SP"]
    right_inputs_student_id_1 = ["Joana", "Silveira", "17-02-1972", "434.763.780-20", "Felicidade, 14", "Ap. 201",
                                 "Rio de Janeiro", "RJ"]

    def setUp(self):
        self.erp_instance = Erp()
        self.assertEqual(len(self.erp_instance.students), 0)

    def test_add_1_student_passes(self):
        with mock.patch('builtins.input', side_effect=self.right_inputs_student_id_0):
            self.erp_instance.add_student()
        self.assertEqual(self.erp_instance.students[0], self.right_inputs_student_id_0)

    def test_add_2_students_passes(self):
        with mock.patch('builtins.input', side_effect=self.right_inputs_student_id_0):
            self.erp_instance.add_student()
        self.assertEqual(self.erp_instance.students[0], self.right_inputs_student_id_0)
        self.assertEqual(len(self.erp_instance.students), 1)
        with mock.patch('builtins.input', side_effect=self.right_inputs_student_id_1):
            self.erp_instance.add_student()
        self.assertEqual(self.erp_instance.students[1], self.right_inputs_student_id_1)
        self.assertEqual(self.erp_instance.students, [self.right_inputs_student_id_0, self.right_inputs_student_id_1])

    def test_add_1_student_fails_numbers_in_string(self):
        wrong_input = "João2"
        inputed_inputs = self.right_inputs_student_id_0[:]
        inputed_inputs.insert(0, wrong_input)  # inserting wrong input
        expected_exception = "Invalid input. The name muss contain only letter or spaces."
        self.held, sys.stdout = sys.stdout, StringIO()
        with mock.patch('builtins.input', side_effect=inputed_inputs):
            self.erp_instance.add_student()
        self.assertEqual(self.erp_instance.students[-1], self.right_inputs_student_id_0)
        printed_messages = sys.stdout.getvalue()
        self.assertIn(expected_exception, printed_messages)
        self.held, sys.stdout = None, None

    def test_add_1_student_fails_type_error(self):
        wrong_input = 2
        inputed_inputs = self.right_inputs_student_id_0[:]
        inputed_inputs.insert(0, wrong_input)  # inserting wrong input
        with mock.patch('builtins.input', side_effect=inputed_inputs):
            with self.assertRaises(TypeError):
                self.erp_instance.add_student()

    def test_add_1_student_fails_type_error2(self):
        wrong_input = 2
        inputed_inputs = ["João", "da Silva", "23-05-1978", wrong_input, "297.586.890-10", "Rua Bom Sucesso, 487",
                          "Casa", "São Paulo", "SP"]
        with self.assertRaises(TypeError):
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.erp_instance.add_student()

    def test_add_1_student_fails_type_error3(self):
        wrong_input = True
        inputed_inputs = ["João", "da Silva", "23-05-1978", "297.586.890-10", "Rua Bom Sucesso, 487", wrong_input,
                          "Casa", "São Paulo", "SP"]
        with mock.patch('builtins.input', side_effect=inputed_inputs):
            with self.assertRaises(TypeError):
                self.erp_instance.add_student()

    def test_add_1_student_fails_type_error4(self):
        wrong_input = 3
        inputed_inputs = ["João", "da Silva", "23-05-1978", "297.586.890-10", wrong_input, "Casa", "São Paulo", "SP"]
        with mock.patch('builtins.input', side_effect=inputed_inputs):
            with self.assertRaises(TypeError):
                self.erp_instance.add_student()

    def tearDown(self):
        self.erp_instance = None


if __name__ == "__main__":
    unittest.main()
