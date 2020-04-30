from validators.validators import Validators

class ConsoleGetter():

    @staticmethod
    def get_customer_forename():
        customer_forename = input("Enter the customer's forename: ")
        validated_customer_forename = Validators().validate_customer_forename(customer_forename)
        return validated_customer_forename

    @staticmethod
    def get_customer_surname():
        customer_surname = input("Enter the customer's surname: ")
        validated_customer_surname = Validators().validate_customer_surname(customer_surname)
        return validated_customer_surname

    @staticmethod
    def get_customer_birthday():
        customer_birthdate = input("Enter the customer's birthday (DD-MM-YYYY): ")
        validated_customer_birthday = Validators().validate_customer_birthdate(customer_birthdate)
        return validated_customer_birthday

    @staticmethod
    def get_customer_personal_id():
        customer_personal_id = input("Enter the customer's ID number: ")
        validated_customer_personal_id = Validators().validate_personal_id(customer_personal_id)
        return validated_customer_personal_id

    @staticmethod
    def get_customer_address_street_and_number():
        customer_address_street_and_number = input("Enter the customer's street and street number: ")
        validated_customer_address_street_and_number = Validators().validate_customer_address_street_and_number(customer_address_street_and_number)
        return validated_customer_address_street_and_number

    @staticmethod
    def get_customer_address_other():
        customer_address_others = input("Enter other address information (NA = Not applies): ")
        validated_customer_address_others = Validators().validate_customer_address_others(
            customer_address_others)
        return validated_customer_address_others

    @staticmethod
    def get_customer_address_city():
        customer_address_city = input("Enter the customer's city: ")
        validated_customer_address_city = Validators().validate_customer_adress_city(customer_address_city)
        return validated_customer_address_city

    @staticmethod
    def get_customer_address_state():
        customer_address_state = input("Enter the customer's state: ")
        validated_customer_address_state = Validators().validate_customer_adress_state(customer_address_state)
        return validated_customer_address_state
