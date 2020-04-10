from ConsoleGetter import ConsoleGetter
from ConsoleRemover import ConsoleRemover

class ClassesManagementSystem():


	def __init__(self):
		self.students = []

	def add_student(self):
		student_forename = ConsoleGetter().get_student_forename()
		student_surname = ConsoleGetter().get_student_surname()
		student_birthday = ConsoleGetter().get_student_birthday()
		student_id_number = ConsoleGetter().get_student_id_number()
		student_adress_street_and_number = ConsoleGetter().get_student_adress_street_and_number()
		student_adress_others = ConsoleGetter().get_student_adress_others()
		student_adress_city = ConsoleGetter().get_student_adress_city()
		student_adress_state = ConsoleGetter().get_student_adress_state()
		
		student_register = [student_forename, student_surname, student_birthday, student_id_number, student_adress_street_and_number, student_adress_others, student_adress_city, student_adress_state]

		self.students.append(student_register)
	
	def remove_student_by_index(self):
		
		max_range = len(self.students)
		student_id = int(ConsoleRemover().remove_student_by_index(max_range))
		del self.students[student_id]

	def remove_student_by_name(self):
		return 1
	
	def add_classes(self):
		pass
	
	def remove_classes(self):
		pass

if __name__ == "__main__":
	system = ClassesManagementSystem()
	system.remove_student_by_index()