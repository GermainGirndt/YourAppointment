from console.console_getter  import ConsoleGetter
from console.console_remover import ConsoleRemover
from datetime import datetime
import sqlite3


class AppointmentsManagementSystem():

	def __init__(self):
		self.customers_registry = []

	def add_customer_to_registry(self):
		new_customer = self.add_new_customer()
		customer_data = new_customer.return_customer_data()
		self.customers_registry.append(customer_data)

	def add_new_customer(self):
		new_customer = customer()
		return new_customer

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
			CUSTOMER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            FORENAME TEXT,
            SURNAME TEXT,
            BIRTHDATE TEXT,
            PERSONAL_ID TEXT,
            ADDRESS_STREET_AND_NUMBER TEXT,
            ADDRESS_OTHER TEXT,
            ADDRESS_CITY TEXT,
            ADDRESS_STATE TEXT,
            REGISTER_DATE TEXT,
            REGISTER_TIME TEXT,
            STATUS TEXT
            )""")

		c.execute("""INSERT INTO customers(
			FORENAME,
            SURNAME,
            BIRTHDATE,
            PERSONAL_ID,
            ADDRESS_STREET_AND_NUMBER,
            ADDRESS_OTHER,
            ADDRESS_CITY,
            ADDRESS_STATE,
            REGISTER_DATE,
            REGISTER_TIME,
            STATUS
            ) VALUES (:fn, :sn, :bd, :in, :asn, :ao, :ac, :as, :rd, :rt, :st)""",
				  {'fn': new_customer.forename, 'sn': new_customer.surname,
				   'bd':new_customer.birthday, 'in': new_customer.personal_id,
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
		self.personal_id = ConsoleGetter().get_customer_personal_id()
		self.address_street_and_number = ConsoleGetter().get_customer_address_street_and_number()
		self.address_other = ConsoleGetter().get_customer_address_other()
		self.address_city = ConsoleGetter().get_customer_address_city()
		self.address_state = ConsoleGetter().get_customer_address_state()
		self.register_date = datetime.now().strftime("%Y-%m-%d")
		self.register_time = datetime.now().strftime("%H:%M")
		self.status = "Active"

	def return_customer_data(self):
		customer_data = [self.forename, self.surname, self.birthday,
							 self.personal_id, self.address_street_and_number,
							 self.address_other, self.address_city, self.address_state,
							 self.register_date, self.register_time, self.status]
		return customer_data