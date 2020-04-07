
class ClassesManager():


	def __init__(self):
		self.students = []

	def add_student(self):
		student_forename = ConsoleGetter().validateForename()
		student_surname = ConsoleGetter().validateSurname()
		student_birthday = input("Digite a data de nascimento do estudante (DD-MM-AA): ")
		student_cpf = input("Digite o CPF do estudante: ")
		student_adress_street_and_number = input("Digite a rua e o número do local de residência do estudante: ")
		student_adress_others = input("Digite o apartamento ou outra referência (NA = Não aplica): ")
		student_adress_city = input("Digite a cidade do estudante: ")
		student_adress_state = input("Digite o estado do estudante: ")
		
		student_register = [student_forename, student_surname, student_birthday, student_cpf, student_adress_street_and_number, student_adress_others, student_adress_city, student_adress_state]

		self.students.append(student_register)
	
	def remove_student_by_id(self):
		id = input("Entre a Id do estudante a ser excluído: ")
		if not isinstance(id, str):
			raise(TypeError)
		try:
			del self.students[int(id)]
		except(IndexError):
			print(f"The inputed value is out of range. Please input a index from 0 to {len(self.students)}")
			id = input("Entre a Id do estudante a ser excluído: ")
			del self.students[int(id)]

	def removeStudentByName(self):
		return 1
	
	def addClasses(self):
		pass
	
	def removeClasses(self):
		pass


class ConsoleGetter():


	@staticmethod
	def get_forename():
		forename = input("Enter the student's Forename: ")
		validated_forename = Validators().validate_string_alpha_spaces_len25(forename)
		return validated_forename

	@staticmethod
	def get_surname():
		surname = input("Enter the student's Surname: ")
		validated_surname = Validators().validate_string_alpha_spaces_len25(surname)
		return validated_surname


class Validators():


	@staticmethod
	def validate_string_alpha_and_spaces_len25(string_to_validate:str):
		while not Validators().is_alpha_or_has_spaces(string_to_validate) or len(string_to_validate) > 25:
			while not Validators().is_alpha_or_has_spaces(string_to_validate):
				print("Invalid input. The name muss contain only letter or spaces.")
				string_to_validate = input("Enter the student's name: ")
			while len(string_to_validate) > 20:
				print("Invalid input. The name may not be longer than 25 characters.")
				string_to_validate = input("Enter the student's name: ")

		return string_to_validate

	@staticmethod
	def is_alpha_or_has_spaces(forename):
		return True if forename.replace(" ", "").isalpha() else False