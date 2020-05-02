
from validators.validators import Validators

class ConsoleRemover():


	def remove_customer_by_index(self, max_range):
		inputed_customer_index = input("Enter the id of the customer to be removed: ")
		v = Validators(inputed_customer_index)
		validated_customer_index = v.validate_customer_index(max_range)
		return validated_customer_index
