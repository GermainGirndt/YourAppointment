from console.console_getter  import ConsoleGetter
from console.console_remover import ConsoleRemover
from datetime import datetime


class AppointmentsManagementSystem():


	def __init__(self):
		self.students_register = []

	def add_student_to_registry(self):

		student_data = self.get_student_data()
		register_data = self.get_register_data()

		self.students_register.append(student_data + register_data)

	def get_student_data(self):
		new_student = Student()
		return new_student.return_student_data()

	def get_register_data(self):
		student_register_day = datetime.now().strftime("%Y-%m-%d")
		student_register_time = datetime.now().strftime("%H:%M:%S")
		student_register_status = "Active"
		register_data = [student_register_day, student_register_time, student_register_status]
		return register_data

	def remove_student_by_index(self):
		max_range = len(self.students_register)
		student_id = int(ConsoleRemover().remove_student_by_index(max_range))
		del self.students_register[student_id]

	def remove_student_by_name(self):
		return 1
	
	def add_classes(self):
		pass
	
	def remove_classes(self):
		pass


class Student():

	def __init__(self):
		self.student_forename = ConsoleGetter().get_student_forename()
		self.student_surname = ConsoleGetter().get_student_surname()
		self.student_birthday = ConsoleGetter().get_student_birthday()
		self.student_id_number = ConsoleGetter().get_student_id_number()
		self.student_address_street_and_number = ConsoleGetter().get_student_address_street_and_number()
		self.student_address_others = ConsoleGetter().get_student_address_others()
		self.student_address_city = ConsoleGetter().get_student_address_city()
		self.student_address_state = ConsoleGetter().get_student_address_state()

	def return_student_data(self):
		student_register = [self.student_forename, self.student_surname, self.student_birthday, self.student_id_number, self.student_address_street_and_number, self.student_address_others, self.student_address_city, self.student_address_state]
		return student_register


if __name__ == "__main__":
	system = ClassesManagementSystem()
	system.add_student()