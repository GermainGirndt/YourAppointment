from console.console_getter  import ConsoleGetter
from console.console_remover import ConsoleRemover
from datetime import datetime
import sqlite3


class AppointmentsManagementSystem():


	def __init__(self):
		self.customers_register = []

	def add_customer_to_registry(self):

		customer_data = self.get_customer_data()
		register_data = self.get_register_data()

		self.customers_register.append(customer_data + register_data)

	def get_customer_data(self):
		new_customer = customer()
		return new_customer.return_customer_data()

	def get_register_data(self):
		customer_register_day = datetime.now().strftime("%Y-%m-%d")
		customer_register_time = datetime.now().strftime("%H:%M")
		customer_register_status = "Active"
		register_data = [customer_register_day, customer_register_time, customer_register_status]
		return register_data

	def remove_customer_by_index(self):
		max_range = len(self.customers_register)
		customer_id = int(ConsoleRemover().remove_customer_by_index(max_range))
		del self.customers_register[customer_id]

	def remove_customer_by_name(self):
		return 1
	
	def add_classes(self):
		pass
	
	def remove_classes(self):
		pass

	def add_new_customer_to_database(self):
		new_customer = customer()
		conn = sqlite3.connect('YourAppointment.db')
		c = conn.cursor()
		c.execute("""CREATE TABLE customers (
             forename text,
             surname text,
             birthdate text,
             id_num text,
             address_street_and_number text,
             address_other text,
             address_city text,
             address_state text,
             register_date text,
             register_time text,
             status text
             )""")
		c.execute("INSERT INTO customers VALUES (:fn, :sn, :bd, :in, :asn, :ao, :ac, :as, :rd, :rt, :st)",
				  {'fn': new_customer.customer_forename, 'sn': new_customer.customer_surname,
				   'bd':new_customer.customer_birthday, 'in': new_customer.customer_id_number,
				   'asn': new_customer.customer_address_street_and_number,
				   'ao': new_customer.customer_address_other, 'ac': new_customer.customer_address_city,
				   'as': new_customer.customer_address_state, 'rd': new_customer.customer_register_date,
				   'rt': new_customer.customer_register_time, 'st': new_customer.customer_status})
		conn.commit()
		conn.close()




class customer():

	def __init__(self):
		self.customer_forename = ConsoleGetter().get_customer_forename()
		self.customer_surname = ConsoleGetter().get_customer_surname()
		self.customer_birthday = ConsoleGetter().get_customer_birthday()
		self.customer_id_number = ConsoleGetter().get_customer_id_number()
		self.customer_address_street_and_number = ConsoleGetter().get_customer_address_street_and_number()
		self.customer_address_other = ConsoleGetter().get_customer_address_other()
		self.customer_address_city = ConsoleGetter().get_customer_address_city()
		self.customer_address_state = ConsoleGetter().get_customer_address_state()
		self.customer_register_date = datetime.now().strftime("%Y-%m-%d")
		self.customer_register_time = datetime.now().strftime("%H:%M")
		self.customer_status = "Active"

	def return_customer_data(self):
		customer_register = [self.customer_forename, self.customer_surname, self.customer_birthday, self.customer_id_number, self.customer_address_street_and_number, self.customer_address_other, self.customer_address_city, self.customer_address_state]
		return customer_register


if __name__ == "__main__":
	system = ClassesManagementSystem()
	system.add_customer()