import set_test_path
import unittest
from unittest import mock
from io import StringIO
from contextlib import redirect_stdout
from app import ClassesManagementSystem as Erp

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

    def test_add_1_student_fails_forename_value_error(self):
        wrong_forename_input = "João2"
        inputed_inputs = self.right_inputs_student_id_0[:]
        inputed_inputs.insert(0, wrong_forename_input)
        expected_exception = "Invalid input. The forename muss contain only letters or spaces.\n"
        with redirect_stdout(StringIO()) as stdout:
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.erp_instance.add_student()
        self.assertEqual(self.erp_instance.students[-1], self.right_inputs_student_id_0)
        printed_messages = stdout.getvalue()
        self.assertIn(expected_exception, printed_messages)


    def test_add_1_student_fails_surname_value_error(self):
        wrong_surname_input = "da Silva2"
        inputed_inputs = self.right_inputs_student_id_0[:]
        inputed_inputs.insert(1, wrong_surname_input)
        expected_exception = "Invalid input. The surname muss contain only letters or spaces.\n"
        with redirect_stdout(StringIO()) as stdout:
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.erp_instance.add_student()
        self.assertEqual(self.erp_instance.students[-1], self.right_inputs_student_id_0)
        printed_messages = stdout.getvalue()
        self.assertIn(expected_exception, printed_messages)

    def test_add_1_student_fails_birthdate(self):
        wrong_birthdate_input = "24011978"
        inputed_inputs = self.right_inputs_student_id_0[:]
        inputed_inputs.insert(2, wrong_birthdate_input)
        expected_exception = "Invalid input. The birthdate muss comply to the required format\n"
        with redirect_stdout(StringIO()) as stdout:
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.erp_instance.add_student()
        self.assertEqual(self.erp_instance.students[-1], self.right_inputs_student_id_0)
        printed_messages = stdout.getvalue()
        self.assertIn(expected_exception, printed_messages)


    def test_add_1_student_fails_student_id(self):
        wrong_student_id_input = "24011978"
        inputed_inputs = self.right_inputs_student_id_0[:]
        inputed_inputs.insert(3, wrong_student_id_input)
        expected_exception = "Invalid input. The student id muss have 11 digits and comply to the required format\n"
        with redirect_stdout(StringIO()) as stdout:
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.erp_instance.add_student()
        self.assertEqual(self.erp_instance.students[-1], self.right_inputs_student_id_0)
        printed_messages = stdout.getvalue()
        self.assertIn(expected_exception, printed_messages)


    def test_add_1_student_fails_student_id2(self):
        wrong_student_id_input = "1234567891!"
        inputed_inputs = self.right_inputs_student_id_0[:]
        inputed_inputs.insert(3, wrong_student_id_input)
        expected_exception = "Invalid input. The id number may only have numbers, points and dashes\n"
        with redirect_stdout(StringIO()) as stdout:
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.erp_instance.add_student()
        self.assertEqual(self.erp_instance.students[-1], self.right_inputs_student_id_0)
        printed_messages = stdout.getvalue()
        self.assertIn(expected_exception, printed_messages)


    def test_add_1_student_fails_address_street_and_number(self):
        wrong_address_street_and_number_input = "XX Street !"
        inputed_inputs = self.right_inputs_student_id_0[:]
        inputed_inputs.insert(4, wrong_address_street_and_number_input)
        expected_exception = "Invalid input. The address may not contain special caracteres.\n"
        with redirect_stdout(StringIO()) as stdout:
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.erp_instance.add_student()
        self.assertEqual(self.erp_instance.students[-1], self.right_inputs_student_id_0)
        printed_messages = stdout.getvalue()
        self.assertIn(expected_exception, printed_messages)


    def test_add_1_student_fails_type_error(self):
        wrong_student_name_input = 2
        inputed_inputs = self.right_inputs_student_id_0[:]
        inputed_inputs.insert(0, wrong_student_name_input)
        with self.assertRaises(TypeError):
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.erp_instance.add_student()

    def test_add_1_student_fails_type_error2(self):
        wrong_student_id_input = 2
        inputed_inputs = self.right_inputs_student_id_0[:]
        inputed_inputs.insert(3, wrong_student_id_input)
        with self.assertRaises(TypeError):
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.erp_instance.add_student()

    def test_add_1_student_fails_type_error3(self):
        wrong_address_other_input = True
        inputed_inputs = self.right_inputs_student_id_0[:]
        inputed_inputs.insert(6, wrong_address_other_input)
        with self.assertRaises(TypeError):
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.erp_instance.add_student()


    def test_add_1_student_fails_type_error4(self):
        wrong_address_street_and_number_input = 3
        inputed_inputs = self.right_inputs_student_id_0[:]
        inputed_inputs.insert(4, wrong_address_street_and_number_input)
        with self.assertRaises(TypeError):
            with mock.patch('builtins.input', side_effect=inputed_inputs):
                self.erp_instance.add_student()

    def tearDown(self):
        self.erp_instance = None

if __name__ == "__main__":
    unittest.main()