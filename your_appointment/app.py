from console.console_getter  import ConsoleGetter
from console.console_remover import ConsoleRemover
from datetime import datetime
import sqlite3


class AppointmentsManagementSystem():


	def __init__(self):
		self.customers_registry = []

	def add_customer_to_registry(self):

		customer_data = self.get_customer_data()
		register_data = self.get_register_data()

		self.customers_registry.append(customer_data + register_data)

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
		max_range = len(self.customers_registry)
		customer_id = int(ConsoleRemover().remove_customer_by_index(max_range))
		del self.customers_registry[customer_id]

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
				  {'fn': new_customer.forename, 'sn': new_customer.surname,
				   'bd':new_customer.birthday, 'in': new_customer.id_number,
				   'asn': new_customer.address_street_and_number,
				   'ao': new_customer.address_other, 'ac': new_customer.address_city,
				   'as': new_customer.address_state, 'rd': new_customer.register_date,
				   'rt': new_customer.register_time, 'st': new_customer.status})
		conn.commit()
		conn.close()




class customer():

	def __init__(self):
		self.forename = ConsoleGetter().get_customer_forename()
		self.surname = ConsoleGetter().get_customer_surname()
		self.birthday = ConsoleGetter().get_customer_birthday()
		self.id_number = ConsoleGetter().get_customer_id_number()
		self.address_street_and_number = ConsoleGetter().get_customer_address_street_and_number()
		self.address_other = ConsoleGetter().get_customer_address_other()
		self.address_city = ConsoleGetter().get_customer_address_city()
		self.address_state = ConsoleGetter().get_customer_address_state()
		self.register_date = datetime.now().strftime("%Y-%m-%d")
		self.register_time = datetime.now().strftime("%H:%M")
		self.status = "Active"

	def return_customer_data(self):
		customer_register = [self.forename, self.surname, self.birthday,
							 self.id_number, self.address_street_and_number,
							 self.address_other, self.address_city, self.address_state]
		return customer_register


if __name__ == "__main__":
	system = ClassesManagementSystem()
	system.add_customer()