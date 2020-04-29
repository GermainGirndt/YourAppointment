import datetime

class Validators():


    @staticmethod
    def raise_type_error_if_not_string(inputedValue):
        if not isinstance(inputedValue,str):
            raise TypeError(f"The value '{inputedValue}' is not a string")

    @staticmethod
    def raise_value_error_if_not_numeric(inputedValue):
        if not inputedValue.isnumeric():
            raise ValueError(f"The value '{inputedValue}' is not numeric")

    @staticmethod
    def is_alpha_or_has_spaces(string_to_validate):
        return True if string_to_validate.replace(" ", "").isalpha() else False

    @staticmethod
    def is_alphanumeric_or_has_spaces_dots_commas_and_dashes(string_to_validate):
        return True if string_to_validate.replace(" ", "").replace(",","").replace(".","").replace("-","").isalnum() else False

    @staticmethod
    def validate_alpha_and_spaces_len25(string_to_validate):
        Validators().raise_type_error_if_not_string(string_to_validate)
        checks = 0
        while checks < 2:
            while not Validators().is_alpha_or_has_spaces(string_to_validate):
                checks = 0
                print("Invalid input. The name may only contain letter or spaces.")
                string_to_validate = input("Enter the customer's name: ")
            checks += 1
            while len(string_to_validate) > 25:
                checks = 0
                print("Invalid input. The name may not be longer than 25 characters.")
                string_to_validate = input("Enter the customer's name: ")
            checks += 1
        Validators().raise_type_error_if_not_string(string_to_validate)
        return string_to_validate


    @staticmethod
    def validate_customer_forename(customer_forename_to_validate):
        Validators().raise_type_error_if_not_string(customer_forename_to_validate)
        checks = 0
        while checks < 2:
            while not Validators().is_alpha_or_has_spaces(customer_forename_to_validate):
                checks = 0
                print("Invalid input. The forename may only contain letter or spaces.")
                customer_forename_to_validate = input("Enter the customer's forename: ")
                Validators().raise_type_error_if_not_string(customer_forename_to_validate)
            checks += 1
            while len(customer_forename_to_validate) > 20:
                checks = 0
                print("Invalid input. The forename may not be longer than 25 characters.")
                customer_forename_to_validate = input("Enter the customer's forename: ")
                Validators().raise_type_error_if_not_string(customer_forename_to_validate)
            checks += 1
        Validators().raise_type_error_if_not_string(customer_forename_to_validate)
        return customer_forename_to_validate


    @staticmethod
    def validate_customer_surname(customer_surname_to_validate):
        Validators().raise_type_error_if_not_string(customer_surname_to_validate)
        checks = 0
        while checks < 2:
            while not Validators().is_alpha_or_has_spaces(customer_surname_to_validate):
                checks = 0
                print("Invalid input. The surname may only contain letter or spaces.")
                customer_surname_to_validate = input("Enter the customer's surname: ")
                Validators().raise_type_error_if_not_string(customer_surname_to_validate)
            checks += 1
            while len(customer_surname_to_validate) > 20:
                checks = 0
                print("Invalid input. The surname may not be longer than 25 characters.")
                customer_surname_to_validate = input("Enter the customer's surname: ")
                Validators().raise_type_error_if_not_string(customer_surname_to_validate)
            checks += 1
        return customer_surname_to_validate

    @staticmethod
    def validate_customer_birthdate(date_to_validate):
        Validators().raise_type_error_if_not_string(date_to_validate)
        while True:
            try:
                datetime.datetime.strptime(date_to_validate, '%d-%m-%Y')
            except ValueError:
                print("Invalid input. The birthdate muss comply to the required format")
                date_to_validate = input("Enter the customer's birthday (DD-MM-YYYY): ")
                Validators().raise_type_error_if_not_string(date_to_validate)
            else:
                return date_to_validate #noy using validated_date because it would be a datatime object

    @staticmethod
    def validate_id_number(id_number_to_validate):
        Validators().raise_type_error_if_not_string(id_number_to_validate)
        checks = 0
        while checks < 2:
            while len(id_number_to_validate.replace("-","").replace(".","")) != 11:
                checks = 0
                print(f"Invalid input. The customer id muss have 11 digits and comply to the required format")
                id_number_to_validate = input("Enter the customer's birthname (DD-MM-YYYY): ")
                Validators().raise_type_error_if_not_string(id_number_to_validate)
            checks += 1
            while not id_number_to_validate.replace("-","").replace(".","").isnumeric():
                checks = 0
                print(f"Invalid input. The id number may only have numbers, points and dashes")
                id_number_to_validate = input("Enter the customer's birthname (DD-MM-YYYY): ")
                Validators().raise_type_error_if_not_string(id_number_to_validate)
            checks += 1
        return id_number_to_validate

    @staticmethod
    def validate_customer_address_street_and_number(address_street_and_number_to_validate):
        Validators().raise_type_error_if_not_string(address_street_and_number_to_validate)
        checks = 0
        while checks < 2:
            while not Validators().is_alphanumeric_or_has_spaces_dots_commas_and_dashes(address_street_and_number_to_validate):
                checks = 0
                print("Invalid input. The address may not contain special caracters.")
                address_street_and_number_to_validate = input("Enter the customer's street and number: ")
            checks += 1
            while len(address_street_and_number_to_validate) > 25:
                checks = 0
                print("Invalid input. The address may not be longer than 25 characters.")
                address_street_and_number_to_validate = input("Enter the customer's street and number: ")
            checks += 1
        Validators().raise_type_error_if_not_string(address_street_and_number_to_validate)
        return address_street_and_number_to_validate


    @staticmethod
    def validate_customer_address_others(address_others_to_validate):
        Validators().raise_type_error_if_not_string(address_others_to_validate)
        checks = 0
        while checks < 2:
            while not Validators().is_alphanumeric_or_has_spaces_dots_commas_and_dashes(address_others_to_validate):
                checks = 0
                print("Invalid input. The address may not contain special caracters.")
                address_others_to_validate = input("Enter the customer's street and number: ")
            checks += 1
            while len(address_others_to_validate) > 25:
                checks = 0
                print("Invalid input. The address may not be longer than 25 characters.")
                address_others_to_validate = input("Enter the customer's street and number: ")
            checks += 1
        Validators().raise_type_error_if_not_string(address_others_to_validate)
        return address_others_to_validate


    @staticmethod
    def validate_customer_adress_city(customer_adress_city_to_validate):
        Validators().raise_type_error_if_not_string(customer_adress_city_to_validate)
        checks = 0
        while checks < 2:
            while not Validators().is_alpha_or_has_spaces(customer_adress_city_to_validate):
                checks = 0
                print("Invalid input. The city name may only contain letter or spaces.")
                customer_adress_city_to_validate = input("Enter the customer's city name: ")
                Validators().raise_type_error_if_not_string(customer_adress_city_to_validate)
            checks += 1
            while len(customer_adress_city_to_validate) > 25:
                checks = 0
                print("Invalid input. The city name may not be longer than 25 characters.")
                customer_adress_city_to_validate = input("Enter the customer's city name: ")
                Validators().raise_type_error_if_not_string(customer_adress_city_to_validate)
            checks += 1
        Validators().raise_type_error_if_not_string(customer_adress_city_to_validate)
        return customer_adress_city_to_validate

    @staticmethod
    def validate_customer_adress_state(customer_adress_state_to_validate):
        Validators().raise_type_error_if_not_string(customer_adress_state_to_validate)
        checks = 0
        while checks < 2:
            while not Validators().is_alpha_or_has_spaces(customer_adress_state_to_validate):
                checks = 0
                print("Invalid input. The state name may only contain letter or spaces.")
                customer_adress_state_to_validate = input("Enter the customer's state name: ")
                Validators().raise_type_error_if_not_string(customer_adress_state_to_validate)
            checks += 1
            while len(customer_adress_state_to_validate) > 25:
                checks = 0
                print("Invalid input. The state name may not be longer than 25 characters.")
                customer_adress_state_to_validate = input("Enter the customer's state name: ")
                Validators().raise_type_error_if_not_string(customer_adress_state_to_validate)
            checks += 1
        Validators().raise_type_error_if_not_string(customer_adress_state_to_validate)
        return customer_adress_state_to_validate