
class ClassesManager():

	students = []

	def addStudent(self):
		student_Forename = input("Digite o nome do estudante: ")
		student_Surname = input("Digite o sobrenome do estudante: ")
		student_Birthday = input("Digite a data de nascimento do estudante (DD-MM-AA): ")
		student_CPF = input("Digite o CPF do estudante: ")
		student_Adress_StreetAndNumber = input("Digite a rua e o número do local de residência do estudante: ")
		student_Adress_Others = input("Digite o apartamento ou outra referência (NA = Não aplica): ")
		student_Adress_City = input("Digite a cidade do estudante: ")
		student_Adress_State = input("Digite o estado do estudante: ")
		
		student_Register = [student_Forename, student_Surname, student_Birthday, student_CPF, student_Adress_StreetAndNumber, student_Adress_Others, student_Adress_City, student_Adress_State]

		ClassesManager().students.append(student_Register)

		print(test)


	def removeStudent():
		pass
		
	def addClasses():
		pass
	
	def removeClasses():
		pass

	def addStudent():
		pass
	
	def removeStudent():
		pass



