from Validators import Validators

class ConsoleRemover():


	def remove_student_by_index(self, max_range):


		inputed_student_index = input("Enter the index of the student to be removed: ")
		Validators().raise_type_error_if_not_string(inputed_student_index)
		if max_range == 0:
			print("There are no students to be removed.")
		else:
			while not (0 <= int(inputed_student_index) <= max_range) :
				print(f"The inputed value is out of range. Please input a index from 0 to {max_range}")
				inputed_student_index = input("Enter the inputed_student_index of the student to be excluded: ")
				Validators().raise_type_error_if_not_string(inputed_student_index)
			return inputed_student_index
