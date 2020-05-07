from console.console_getter  import ConsoleGetter
from console.console_remover import ConsoleRemover
from classes.customer import Customer
from classes.appointment import Appointment
from datetime import datetime
import sqlite3


class DataManager():

	def __init__(self):
		self.customers_registry = []
		self.db = Database()

	def add_customer_to_registry(self):
		new_customer = self.add_new_customer()
		customer_data = new_customer.return_customer_data()
		self.customers_registry.append(customer_data)

	def add_new_customer(self):
		new_customer = Customer()
		return new_customer

	def remove_customer_by_index(self):
		max_range = len(self.customers_registry)
		customer_id = int(ConsoleRemover().remove_customer_by_index(max_range))
		del self.customers_registry[customer_id - 1] #The registry starts by 0 | the ID by 1

	def add_new_customer_to_database(self):
		new_customer = Customer()
		self.db.add_new_customer(new_customer)

	def add_new_appointment_to_database(self):
		new_appointment = Appointment()
		self.db.add_new_appointment(new_appointment)

	def fetchone(self):
		customer = self.db.fetchone("customers")
		return customer


class Database():

	def __init__(self):
		self.conn = sqlite3.connect('YourAppointment.db')
		self.c = self.conn.cursor()

	def set_cursor(self):
		return self.c

	def commit_and_close(self):
		self.conn.commit()
		self.conn.close()

	def create_table_customers(self):
		self.c.execute("""CREATE TABLE IF NOT EXISTS customers (
					CUSTOMER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
		            FORENAME TEXT,
		            SURNAME TEXT,
		            FULLNAME TEXT,
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

		try:
			self.c.execute(f"SELECT * FROM customers")
			print(f"Customers Table Created!")
		except:
			print("An error ocurred by the creation from a table")

	def create_table_appointments(self):
		self.c.execute("PRAGMA foreign_keys = ON;")
		self.c.execute("""CREATE TABLE IF NOT EXISTS appointments (
					APPOINTMENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
		            CUSTOMER_ID INTEGER,
		            DAY TEXT,
		            DURATION TEXT,
		            REGISTER_DATE TEXT,
		            REGISTER_TIME TEXT,
		            STATUS TEXT,
		            FOREIGN KEY(CUSTOMER_ID) REFERENCES customers (CUSTOMER_ID)
		            );""")

		try:
			self.c.execute(f"SELECT * FROM customers;")
			print(f"Appointments Table Created!")
		except:
			print("An error ocurred by the creation from a table")


	def fetchone(self, table):
		self.c.execute(f"SELECT * FROM {table}")
		obj = self.c.fetchone()
		return obj

	def fetchall(self, table):
		self.c.execute(f"SELECT * FROM {table}")
		obj = self.c.fetchall()
		return obj

	def select_by_customer_id(self, table, customer_id):
		self.c.execute(f"SELECT * FROM 	{table} WHERE CUSTOMER_ID = {customer_id}")
		obj = self.c.fetchall()
		return obj

	def select_by_fullname(self, table, fullname):
		self.c.execute(f"SELECT * FROM 	{table} WHERE FULLNAME = '{fullname}'")
		obj = self.c.fetchall()
		return obj

	def select_by_forename(self, table, forename):
		self.c.execute(f"SELECT * FROM 	{table} WHERE FORENAME = '{forename}'")
		obj = self.c.fetchall()
		return obj

	def select_entry_by_value(self, table, column, value):
		self.c.execute(f"SELECT * FROM 	{table} WHERE {column} = '{value}'")
		obj = self.c.fetchall()
		return obj

	def exclude_customer_by_id(self, customer_id):
		customer_id = str(customer_id)
		self.conn = sqlite3.connect('YourAppointment.db')
		self.c.execute("SELECT * FROM customers")
		self.c.execute(f"UPDATE customers SET STATUS = 'Inactive' WHERE CUSTOMER_ID = {customer_id}")
		self.c.execute(f"SELECT * FROM customers WHERE CUSTOMER_ID = '{customer_id}'")
		obj = self.c.fetchall()
		print(f"Customer updated to {obj}")


	def add_new_customer(self, new_customer):
		self.c.execute("""INSERT INTO customers(
					FORENAME,
		            SURNAME,
		            FULLNAME,
		            BIRTHDATE,
		            PERSONAL_ID,
		            ADDRESS_STREET_AND_NUMBER,
		            ADDRESS_OTHER,
		            ADDRESS_CITY,
		            ADDRESS_STATE,
		            REGISTER_DATE,
		            REGISTER_TIME,
		            STATUS
		            ) VALUES (:fn, :sn, :fln, :bd, :pid, :asn, :ao, :ac, :as, :rd, :rt, :st)""",
				  {'fn': new_customer.forename, 'sn': new_customer.surname, 'fln': new_customer.fullname,
				   'bd': new_customer.birthday, 'pid': new_customer.personal_id,
				   'asn': new_customer.address_street_and_number,
				   'ao': new_customer.address_other, 'ac': new_customer.address_city,
				   'as': new_customer.address_state, 'rd': new_customer.register_date,
				   'rt': new_customer.register_time, 'st': new_customer.status})

		try:
			self.c.execute(f"SELECT * FROM customers WHERE CUSTOMER_ID = (SELECT max(CUSTOMER_ID) FROM customers);")
			obj = self.c.fetchone()
			print(f"Last customer added:{obj}")
		except:
			print("An error ocurred by inserting the customer to the table")


	def add_new_appointment(self, new_appointment):
		self.c.execute("""INSERT INTO appointments(
					CUSTOMER_ID,
		            DAY,
		            DURATION,
		            REGISTER_DATE,
		            REGISTER_TIME,
		            STATUS
		            ) VALUES (:cid, :day, :dur, :rd, :rt, :st)""",
				  { 'cid': new_appointment.customer_id, 'day': new_appointment.day,
					'dur': new_appointment.duration, 'rd': new_appointment.register_date,
				   'rt': new_appointment.register_time, 'st': new_appointment.status})
		try:
			self.c.execute(f"SELECT * FROM appointments WHERE APPOINTMENT_ID = (SELECT max(APPOINTMENT_ID) FROM appointments)")
			obj = self.c.fetchone()
			print(f"Last appointment added: {obj}")
		except:
			print("An error ocurred by inserting the appointment to the table")


