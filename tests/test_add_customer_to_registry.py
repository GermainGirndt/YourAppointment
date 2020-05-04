import set_test_path
import unittest
from unittest import mock
from io import StringIO
from contextlib import redirect_stdout
from datetime import datetime
from data_manager import DataManager as Dm
from test_resources import TestResourcesCustomer

class test_add_customer_to_memory(TestResourcesCustomer, unittest.TestCase):


    def setUp(self):
        self.dm_instance = Dm()
        self.quick_test_if_num_of_customers_in_registry_equals(0)


    def test_add_costumer_id_1_to_registry_passes(self):
        self.quick_test_add_customer_to_registry(
            inputs=self.RIGHT_INPUTS_CUSTOMER_ID_1,
            expected_return=self.RIGHT_RETURN_CUSTOMER_ID_1
        )

    def test_add_costumer_id_2_to_registry_passes(self):
        self.quick_test_add_customer_to_registry(
            inputs=self.RIGHT_INPUTS_CUSTOMER_ID_2,
            expected_return=self.RIGHT_RETURN_CUSTOMER_ID_2
        )


    def test_add_2_customers_registry_passes(self):
        self.test_add_costumer_id_1_to_registry_passes()
        self.test_add_costumer_id_2_to_registry_passes()
        self.quick_test_if_registry_contain_customers_list(
            list_with_expected_customers=
            [self.RIGHT_RETURN_CUSTOMER_ID_1, self.RIGHT_RETURN_CUSTOMER_ID_2]
        )




    def test_add_1_customer_fails_forename_value_error(self):
        wrong_forename_input = "João2"
        expected_exception = "Invalid input. " \
                             "The customer's forename may only contain letter or spaces.\n"
        self.quick_test_add_customer_handles_value_error(
            right_inputs=self.RIGHT_INPUTS_CUSTOMER_ID_1,
            expected_return=self.RIGHT_RETURN_CUSTOMER_ID_1,
            index_to_insert_the_wrong_input=self.INDEX_OF_FORENAME,
            wrong_input=wrong_forename_input,
            expected_exception=expected_exception
        )


    def test_add_1_customer_fails_surname_value_error(self):
        wrong_surname_input = "da Silva2"
        expected_exception = "Invalid input. " \
                             "The customer's surname may only contain letter or spaces.\n"
        self.quick_test_add_customer_handles_value_error(
            right_inputs=self.RIGHT_INPUTS_CUSTOMER_ID_1,
            expected_return=self.RIGHT_RETURN_CUSTOMER_ID_1,
            index_to_insert_the_wrong_input=self.INDEX_OF_SURNAME,
            wrong_input=wrong_surname_input,
            expected_exception=expected_exception
        )

    def test_add_1_customer_fails_birthdate(self):
        wrong_birthdate_input = "24011978"
        expected_exception = "Invalid input. " \
                             "The customer's birthdate muss comply to the required format\n"
        self.quick_test_add_customer_handles_value_error(
            right_inputs=self.RIGHT_INPUTS_CUSTOMER_ID_1,
            expected_return=self.RIGHT_RETURN_CUSTOMER_ID_1,
            index_to_insert_the_wrong_input=self.INDEX_OF_BIRTHDATE,
            wrong_input=wrong_birthdate_input,
            expected_exception=expected_exception
        )


    def test_add_1_customer_fails_customer_id(self):
        wrong_personal_id_input = "24011978"
        expected_exception = "Invalid input. The customer's personal id muss have 11 digits and " \
                             "comply to the required format\n"
        self.quick_test_add_customer_handles_value_error(
            right_inputs=self.RIGHT_INPUTS_CUSTOMER_ID_1,
            expected_return=self.RIGHT_RETURN_CUSTOMER_ID_1,
            index_to_insert_the_wrong_input=self.INDEX_OF_PERSONAL_ID,
            wrong_input=wrong_personal_id_input,
            expected_exception=expected_exception
        )


    def test_add_1_customer_fails_customer_id2(self):
        wrong_personal_id_input = "1234567891!"
        expected_exception = "Invalid input. The customer's personal id may only have numbers, points and dashes\n"
        self.quick_test_add_customer_handles_value_error(
            right_inputs=self.RIGHT_INPUTS_CUSTOMER_ID_1,
            expected_return=self.RIGHT_RETURN_CUSTOMER_ID_1,
            index_to_insert_the_wrong_input=self.INDEX_OF_PERSONAL_ID,
            wrong_input=wrong_personal_id_input,
            expected_exception=expected_exception
        )

    def test_add_1_customer_fails_address_street_and_number(self):
        wrong_address_street_and_number_input = "XX Street !"
        expected_exception = "Invalid input. The customer's street and number may not contain special caracters.\n"
        self.quick_test_add_customer_handles_value_error(
            right_inputs=self.RIGHT_INPUTS_CUSTOMER_ID_1,
            expected_return=self.RIGHT_RETURN_CUSTOMER_ID_1,
            index_to_insert_the_wrong_input=self.INDEX_OF_ADDRESS_STREET_AND_NUMBER,
            wrong_input=wrong_address_street_and_number_input,
            expected_exception=expected_exception
        )

    def test_add_1_customer_fails_address_street_and_number2(self):
        wrong_address_street_and_number_input = "testing too long adress lalalalala"
        expected_exception = "Invalid input. The customer's street and number may not be longer than 30 characters.\n"
        self.quick_test_add_customer_handles_value_error(
            right_inputs=self.RIGHT_INPUTS_CUSTOMER_ID_1,
            expected_return=self.RIGHT_RETURN_CUSTOMER_ID_1,
            index_to_insert_the_wrong_input=self.INDEX_OF_ADDRESS_STREET_AND_NUMBER,
            wrong_input=wrong_address_street_and_number_input,
            expected_exception=expected_exception
        )

    def test_add_1_customer_fails_address_other(self):
        wrong_address_others_input = "Apartment 101!"
        expected_exception = "Invalid input. The customer's address (other) may not contain special caracters.\n"
        self.quick_test_add_customer_handles_value_error(
            right_inputs=self.RIGHT_INPUTS_CUSTOMER_ID_1,
            expected_return=self.RIGHT_RETURN_CUSTOMER_ID_1,
            index_to_insert_the_wrong_input=self.INDEX_OF_ADDRESS_OTHER,
            wrong_input=wrong_address_others_input,
            expected_exception=expected_exception
        )

    def test_add_1_customer_fails_address_other2(self):
        wrong_address_others_input = "testing too long adress lalalalala"
        expected_exception = "Invalid input. The customer's address (other) may not be longer than 25 characters.\n"
        self.quick_test_add_customer_handles_value_error(
            right_inputs=self.RIGHT_INPUTS_CUSTOMER_ID_1,
            expected_return=self.RIGHT_RETURN_CUSTOMER_ID_1,
            index_to_insert_the_wrong_input=self.INDEX_OF_ADDRESS_OTHER,
            wrong_input=wrong_address_others_input,
            expected_exception=expected_exception
        )

    def test_add_1_customer_fails_address_city(self):
        wrong_address_city_input = "New York 101"
        expected_exception = "Invalid input. The customer's city name may only contain letter or spaces.\n"
        self.quick_test_add_customer_handles_value_error(
            right_inputs=self.RIGHT_INPUTS_CUSTOMER_ID_1,
            expected_return=self.RIGHT_RETURN_CUSTOMER_ID_1,
            index_to_insert_the_wrong_input=self.INDEX_OF_ADDRESS_CITY,
            wrong_input=wrong_address_city_input,
            expected_exception=expected_exception
        )

    def test_add_1_customer_fails_address_city2(self):
        wrong_address_city_input = "testing too long city lalalalalalala"
        expected_exception = "Invalid input. The customer's city name may not be longer than 25 characters.\n"
        self.quick_test_add_customer_handles_value_error(
            right_inputs=self.RIGHT_INPUTS_CUSTOMER_ID_1,
            expected_return=self.RIGHT_RETURN_CUSTOMER_ID_1,
            index_to_insert_the_wrong_input=self.INDEX_OF_ADDRESS_CITY,
            wrong_input=wrong_address_city_input,
            expected_exception=expected_exception
        )

    def test_add_1_customer_fails_address_state(self):
        wrong_address_state_input = "Florida 101"
        expected_exception = "Invalid input. The customer's state name may only contain letter or spaces.\n"
        self.quick_test_add_customer_handles_value_error(
            right_inputs=self.RIGHT_INPUTS_CUSTOMER_ID_1,
            expected_return=self.RIGHT_RETURN_CUSTOMER_ID_1,
            index_to_insert_the_wrong_input=self.INDEX_OF_ADDRESS_STATE,
            wrong_input=wrong_address_state_input,
            expected_exception=expected_exception
        )

    def test_add_1_customer_fails_address_state2(self):
        wrong_address_state_input = "testing too long state lalalalalalala"
        expected_exception = "Invalid input. The customer's state name may not be longer than 25 characters.\n"
        self.quick_test_add_customer_handles_value_error(
            right_inputs=self.RIGHT_INPUTS_CUSTOMER_ID_1,
            expected_return=self.RIGHT_RETURN_CUSTOMER_ID_1,
            index_to_insert_the_wrong_input=self.INDEX_OF_ADDRESS_STATE,
            wrong_input=wrong_address_state_input,
            expected_exception=expected_exception
        )

    def test_add_1_customer_fails_type_error(self):
        wrong_customer_name_input = 2
        self.quick_test_add_customer_raises_type_error(
                right_inputs=self.RIGHT_INPUTS_CUSTOMER_ID_1,
                index_to_insert_the_wrong_input=self.INDEX_OF_FORENAME,
                wrong_input=wrong_customer_name_input
        )

    def test_add_1_customer_fails_type_error2(self):
        wrong_personal_id_input = 2
        self.quick_test_add_customer_raises_type_error(
                right_inputs=self.RIGHT_INPUTS_CUSTOMER_ID_1,
                index_to_insert_the_wrong_input=self.INDEX_OF_PERSONAL_ID,
                wrong_input=wrong_personal_id_input
        )

    def test_add_1_customer_fails_type_error3(self):
        wrong_address_other_input = True
        self.quick_test_add_customer_raises_type_error(
                right_inputs=self.RIGHT_INPUTS_CUSTOMER_ID_1,
                index_to_insert_the_wrong_input=self.INDEX_OF_ADDRESS_OTHER,
                wrong_input=wrong_address_other_input
        )

    def test_add_1_customer_fails_type_error4(self):
        wrong_address_street_and_number_input = 3
        self.quick_test_add_customer_raises_type_error(
                right_inputs=self.RIGHT_INPUTS_CUSTOMER_ID_1,
                index_to_insert_the_wrong_input=self.INDEX_OF_ADDRESS_STREET_AND_NUMBER,
                wrong_input=wrong_address_street_and_number_input
        )


    def test_add_1_customer_fails_type_error5(self):
        wrong_address_state_input = 3
        self.quick_test_add_customer_raises_type_error(
                right_inputs=self.RIGHT_INPUTS_CUSTOMER_ID_1,
                index_to_insert_the_wrong_input=self.INDEX_OF_ADDRESS_STREET_AND_NUMBER,
                wrong_input=wrong_address_state_input
        )

    def tearDown(self):
        self.dm_instance = None

if __name__ == "__main__":
    unittest.main()