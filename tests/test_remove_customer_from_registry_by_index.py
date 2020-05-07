import set_test_path
import unittest
from unittest import mock
from io import StringIO
from contextlib import redirect_stdout
from datetime import datetime
from data_manager import DataManager as Dm
from datetime import datetime
from testing_resources import TestingShortcuts
from test_add_customer_to_registry import TestAddCustomerToRegistry



class test_remove_customer_from_registry_by_index(TestingShortcuts):

	def setUp(self):
		self.dm_instance = Dm()
		self.shortcut_test_if_num_of_customers_in_registry_equals(0)

		self.shortcut_test_add_customer_to_registry(
			inputs=self.RIGHT_INPUTS_CUSTOMER_ID_1,
			expected_return=self.RIGHT_RETURN_CUSTOMER_ID_1
		)
		self.shortcut_test_add_customer_to_registry(
			inputs=self.RIGHT_INPUTS_CUSTOMER_ID_2,
			expected_return=self.RIGHT_RETURN_CUSTOMER_ID_2
		)

		self.shortcut_test_if_registry_contain_customers_list(
			[self.RIGHT_RETURN_CUSTOMER_ID_1, self.RIGHT_RETURN_CUSTOMER_ID_2]
		)

	def test_remove_1_customer_by_index_passes(self):
		id_of_customer_to_be_removed = ["1"]
		self.shortcut_test_remove_customer_list_by_index(
			id_of_customer_to_be_removed=id_of_customer_to_be_removed,
			customer_to_be_removed=self.RIGHT_RETURN_CUSTOMER_ID_1
		)

	def test_remove_1_customer_by_index_passes2(self):
		id_of_customer_to_be_removed = ["2"]
		self.shortcut_test_remove_customer_list_by_index(
			id_of_customer_to_be_removed=id_of_customer_to_be_removed,
			customer_to_be_removed=self.RIGHT_RETURN_CUSTOMER_ID_2
		)



	@unittest.skip("Implement better id orientation")
	def test_remove_2_customers_by_index_passes(self):
		self.test_remove_1_customer_by_index_passes()
		self.test_remove_1_customer_by_index_passes2()
		shortcut_test_if_num_of_customers_in_registry_equals(0)


	def test_remove_1_customer_by_index_fails_inexisting_index(self):
		wrong_customer_id_input = "200"
		right_customer_id_input = ["2"]
		index_to_insert_the_wrong_input = 0
		number_of_customers_in_registry = self.shortcut_get_number_of_customers_in_registry()
		expected_exception = f"Invalid input. The id of the customer to be removed " \
							 f"muss be between 1 and {number_of_customers_in_registry}"

		self.shortcut_test_remove_customer_handles_value_error(
				customer_to_be_removed=self.RIGHT_RETURN_CUSTOMER_ID_2,
				right_inputs_customer_id=right_customer_id_input,
				index_to_insert_the_wrong_input=index_to_insert_the_wrong_input,
				wrong_input=wrong_customer_id_input,
				expected_exception=expected_exception
		)

	def test_remove_1_customer_by_index_fails_value_error(self):
		wrong_customer_id_input = "lalala"
		right_customer_id_input = ["1"]
		index_to_insert_the_wrong_input = 0
		expected_exception = f"Invalid input. The id of the customer to be removed " \
							 f"muss be a number"

		self.shortcut_test_remove_customer_handles_value_error(
				customer_to_be_removed=self.RIGHT_RETURN_CUSTOMER_ID_1,
				right_inputs_customer_id=right_customer_id_input,
				index_to_insert_the_wrong_input=index_to_insert_the_wrong_input,
				wrong_input=wrong_customer_id_input,
				expected_exception=expected_exception
		)

	def test_remove_1_customer_by_index_fails_type_error(self):
		wrong_input = [5]
		self.shortcut_test_remove_customer_raises_type_error(wrong_input)


	def tearDown(self):
		self.dm_instance = None

if __name__ == "__main__":
	unittest.main()