
from validators.validators import Validators

class ConsoleRemover():


	def remove_customer_by_index(self, max_range):


		inputed_customer_index = input("Enter the index of the customer to be removed: ")
		Validators().raise_type_error_if_not_string(inputed_customer_index)
		Validators().raise_value_error_if_not_numeric(inputed_customer_index)
		if max_range == 0:
			print("There are no customers to be removed.")
		else:
			while not (0 <= int(inputed_customer_index) <= max_range) :
				print(f"The inputed value is out of range. Please input a index from 0 to {max_range}")
				inputed_customer_index = input("Enter the inputed_customer_index of the customer to be excluded: ")
				Validators().raise_type_error_if_not_string(inputed_customer_index)
			return inputed_customer_index
