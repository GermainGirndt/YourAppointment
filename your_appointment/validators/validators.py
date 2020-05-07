from datetime import datetime


class Validators():

    def __init__(self, value_to_validate):
        self.checks = 0
        self.value_to_validate = value_to_validate
        self.sanitize_input()

    def sanitize_input(self):
        self.raise_type_error_if_not_string()
        #Enter other sanitizing validators here

    def has_length_less_than(self, max_length):
        while len(self.value_to_validate) >= max_length:
            self.checks = 0
            print(f"Invalid input. The {self.value_name} may not be longer than {max_length} characters.")
            self.value_to_validate = input(f"Enter the {self.value_name}: ")
            self.sanitize_input()
        self.checks += 1

    def raise_type_error_if_not_string(self):
        if not isinstance(self.value_to_validate,str):
            raise TypeError(f"The inputed value is not a string.")
        
    
    def is_numeric(self):
        while not self.value_to_validate.isnumeric():
            self.checks = 0
            print(f"Invalid input. The {self.value_name} muss be a number")
            self.value_to_validate = input(f"Enter the {self.value_name}: ")
            self.sanitize_input()
        self.checks = +1

    def validate_index_max_range(self, max_range):
        if max_range == 0:
            print(f"The are no elements in the index of {self.value_name}")
            return 0
        while True:
            try:
                while not (0 <= int(self.value_to_validate) <= max_range):
                    self.checks = 0
                    print(f"Invalid input. The {self.value_name} muss be between 1 and {max_range}")
                    self.value_to_validate = input(f"Enter the {self.value_name}: ")
                    self.sanitize_input()
            except ValueError:
                self.checks = 0
                self.is_numeric()
            else:
                self.checks += 1
                break
        

    def is_alpha_or_has_spaces(self):
        while not self.value_to_validate.replace(" ", "").isalpha():
            self.checks = 0
            print(f"Invalid input. The {self.value_name} may only contain letter or spaces.")
            self.value_to_validate = input(f"Enter the {self.value_name}: ")
            self.sanitize_input()
        self.checks = 1

    def is_numeric_or_has_dots_and_dashes(self):
        while not self.value_to_validate.replace("-", "").replace(".", "").isnumeric():
            self.checks = 0
            print(f"Invalid input. The {self.value_name} may only have numbers, points and dashes")
            self.value_to_validate = input(f"Enter the {self.value_name}: ")
            self.sanitize_input()
        self.checks += 1



    def is_alphanumeric_or_has_spaces_dots_commas_and_dashes(self):
        while not self.value_to_validate.replace(" ", "").replace(",", "").replace(".", "").replace("-", "").isalnum():
            self.checks = 0
            print(f"Invalid input. The {self.value_name} may not contain special caracters.")
            self.value_to_validate = input(f"Enter the {self.value_name}: ")
            self.sanitize_input()
        self.checks += 1

    def is_date_between(self, min_date_year, max_date_year):
        year_to_validate = int(datetime.strptime(self.value_to_validate, '%d-%m-%Y').year)
        while not (min_date_year < year_to_validate < max_date_year):
            self.checks = 0
            print(f"Invalid input. Insert a valid {self.value_name}")
            self.value_to_validate = input(f"Enter the {self.value_name} (DD-MM-YYYY): ")
            self.sanitize_input()
            self.validate_date()
            year_to_validate = int(datetime.strptime(self.value_to_validate, '%d-%m-%Y').year)
        self.checks += 1

    def validate_date_birthday(self, min_date_year, max_date_year):
        while self.checks < 2:
            self.validate_date()
            self.is_date_between(min_date_year, max_date_year)


    def validate_date(self):
        while True:
            try:
                datetime.strptime(self.value_to_validate, '%d-%m-%Y')
            except ValueError:
                self.checks = 0
                print(f"Invalid input. The {self.value_name} muss comply to the required format")
                self.value_to_validate = input(f"Enter the {self.value_name} (DD-MM-YYYY): ")
                self.sanitize_input()
            else:
                self.checks += 1
                break

    def has_11_digits_or_points_and_dashes(self):
        while len(self.value_to_validate.replace("-", "").replace(".", "")) != 11:
            print(f"Invalid input. The {self.value_name} muss have 11 digits and comply to the required format")
            self.value_to_validate = input(f"Enter the {self.value_name}: ")
            self.sanitize_input()
        self.checks += 1

    def validate_customer_forename(self):
        self.value_name = "customer's forename"
        while self.checks < 2:
            self.is_alpha_or_has_spaces()
            self.has_length_less_than(20)
        return self.value_to_validate

    def validate_customer_surname(self):
        self.value_name = "customer's surname"
        while self.checks < 2:
            self.is_alpha_or_has_spaces()
            self.has_length_less_than(30)
        return self.value_to_validate

    def validate_customer_birthdate(self):
        self.value_name = "customer's birthdate"
        self.validate_date_birthday(1900, 2020)
        sorted_date = datetime.strptime(self.value_to_validate, "%d-%m-%Y").strftime("%Y-%m-%d")
        return sorted_date

    def validate_customer_personal_id(self):
        self.value_name = "customer's personal id"
        while self.checks < 2:
            self.is_numeric_or_has_dots_and_dashes()
            self.has_11_digits_or_points_and_dashes()
        return self.value_to_validate

    def validate_customer_address_street_and_number(self):
        self.value_name = "customer's street and number"
        self.sanitize_input()
        while self.checks < 2:
            self.is_alphanumeric_or_has_spaces_dots_commas_and_dashes()
            self.has_length_less_than(30)
        return self.value_to_validate

    def validate_customer_address_others(self):
        self.value_name = "customer's address (other)"
        while self.checks < 2:
            self.is_alphanumeric_or_has_spaces_dots_commas_and_dashes()
            self.has_length_less_than(25)
        return self.value_to_validate

    def validate_customer_adress_city(self):
        self.value_name = "customer's city name"
        while self.checks < 2:
            self.is_alpha_or_has_spaces()
            self.has_length_less_than(25)
        return self.value_to_validate

    def validate_customer_adress_state(self):
        self.value_name = "customer's state name"
        while self.checks < 2:
            self.is_alpha_or_has_spaces()
            self.has_length_less_than(25)
        return self.value_to_validate
    
    def validate_customer_index(self, max_range):
        self.value_name = "id of the customer to be removed"
        while self.checks < 2:
            self.is_numeric()
            self.validate_index_max_range(max_range)
        return self.value_to_validate


    def validate_selected_input(self, valid_options, choose_option_text):
        self.value_name = "action"
        while self.value_to_validate not in valid_options:
            self.checks = 0
            print(f"Invalid input. {self.value_to_validate} is no valid option")
            self.value_to_validate = input(choose_option_text)
            self.sanitize_input()
        self.checks += 1
        return self.value_to_validate

    def validate_customer_id(self):
        self.value_name = "Customer's ID"
        while not self.value_to_validate.isnumeric():
            self.checks = 0
            print(f"Invalid input. {self.value_to_validate} muss be a number")
            self.value_to_validate = input(f"Enter the {self.value_name}: ")
            self.sanitize_input()
        self.checks += 1
        return self.value_to_validate
