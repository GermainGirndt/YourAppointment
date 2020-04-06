
class ClassesManager():

	def __init__(self):
		self.students = []

	def addStudent(self):
		student_Forename = Validators().validateForename()
		student_Surname = input("Digite o sobrenome do estudante: ")
		student_Birthday = input("Digite a data de nascimento do estudante (DD-MM-AA): ")
		student_CPF = input("Digite o CPF do estudante: ")
		student_Adress_StreetAndNumber = input("Digite a rua e o número do local de residência do estudante: ")
		student_Adress_Others = input("Digite o apartamento ou outra referência (NA = Não aplica): ")
		student_Adress_City = input("Digite a cidade do estudante: ")
		student_Adress_State = input("Digite o estado do estudante: ")
		
		student_Register = [student_Forename, student_Surname, student_Birthday, student_CPF, student_Adress_StreetAndNumber, student_Adress_Others, student_Adress_City, student_Adress_State]

		self.students.append(student_Register)


	def removeStudent():
		pass
		
	def addClasses():
		pass
	
	def removeClasses():
		pass

	def removeStudent():
		pass
	
class Validators():

	@staticmethod
	def validateForename():
		forename = input("Digite o nome do estudante: ")
		if not isinstance(forename, str):
			raise TypeError

		checks = 0
		while not Validators().isAlphaOrHasSpace(forename) or len(forename) > 20:
			while not Validators().isAlphaOrHasSpace(forename):
				print("Invalid input. The name muss contain only letter or spaces.")
				forename = input("Type the student's name: ")
			while len(forename) > 20:
				print("Invalid input. The name may not be longer than 20 characters.")
				forename = input("Type the student's name: ")

		return forename

	@staticmethod
	def isAlphaOrHasSpace(forename):
		if forename.replace(" ", "").isalpha():
			return True
		return False

