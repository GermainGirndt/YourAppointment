from datetime import datetime
from console.console_getter import ConsoleGetter

class Customer():

	def __init__(self):
		self.register_date = datetime.now().strftime("%Y-%m-%d")
		self.register_time = datetime.now().strftime("%H:%M")
		self.status = "Active"
		self.forename = ConsoleGetter().get_customer_forename()
		self.surname = ConsoleGetter().get_customer_surname()
		self.fullname = f"{self.forename} {self.surname}"
		self.birthday = ConsoleGetter().get_customer_birthday()
		self.personal_id = ConsoleGetter().get_customer_personal_id()
		self.address_street_and_number = ConsoleGetter().get_customer_address_street_and_number()
		self.address_other = ConsoleGetter().get_customer_address_other()
		self.address_city = ConsoleGetter().get_customer_address_city()
		self.address_state = ConsoleGetter().get_customer_address_state()

	def return_customer_data(self):
		customer_data = [self.forename, self.surname, self.fullname, self.birthday,
							 self.personal_id, self.address_street_and_number,
							 self.address_other, self.address_city, self.address_state,
							 self.register_date, self.register_time, self.status]
		return customer_data