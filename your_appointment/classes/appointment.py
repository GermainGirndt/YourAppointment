from datetime import datetime
from console.console_getter import ConsoleGetter


class Appointment():

	def __init__(self):
		self.register_date = datetime.now().strftime("%Y-%m-%d")
		self.register_time = datetime.now().strftime("%H:%M")
		self.status = "Active"
		self.customer_id = ConsoleGetter().get_customer_id()
		self.day = ConsoleGetter().get_appointment_day()
		self.duration = ConsoleGetter().get_appointment_duration()

	def return_appointment_data(self):
		appointment_data = [self.customer_id, self.day, self.duration,
							self.register_date, self.register_time, self.status]
		return appointment_data