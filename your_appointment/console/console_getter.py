from validators.validators import Validators

class ConsoleGetter():

    @staticmethod
    def get_customer_forename():
        customer_forename = input("Enter the customer's forename: ")
        v = Validators(customer_forename)
        validated_customer_forename = v.validate_customer_forename()
        return validated_customer_forename

    @staticmethod
    def get_customer_surname():
        customer_surname = input("Enter the customer's surname: ")
        v = Validators(customer_surname)
        validated_customer_surname = v.validate_customer_surname()
        return validated_customer_surname

    @staticmethod
    def get_customer_birthday():
        customer_birthdate = input("Enter the customer's birthday (DD-MM-YYYY): ")
        v = Validators(customer_birthdate)
        validated_customer_birthday = v.validate_customer_birthdate()
        return validated_customer_birthday

    @staticmethod
    def get_customer_personal_id():
        customer_personal_id = input("Enter the customer's ID number: ")
        v = Validators(customer_personal_id)
        validated_customer_personal_id = v.validate_customer_personal_id()
        return validated_customer_personal_id

    @staticmethod
    def get_customer_address_street_and_number():
        customer_address_street_and_number = input("Enter the customer's street and street number: ")
        v = Validators(customer_address_street_and_number)
        validated_customer_address_street_and_number = v.validate_customer_address_street_and_number()
        return validated_customer_address_street_and_number

    @staticmethod
    def get_customer_address_other():
        customer_address_others = input("Enter other address information (NA = Not applies): ")
        v = Validators(customer_address_others)
        validated_customer_address_others = v.validate_customer_address_others()
        return validated_customer_address_others

    @staticmethod
    def get_customer_address_city():
        customer_address_city = input("Enter the customer's city: ")
        v = Validators(customer_address_city)
        validated_customer_address_city = v.validate_customer_adress_city()
        return validated_customer_address_city

    @staticmethod
    def get_customer_address_state():
        customer_address_state = input("Enter the customer's state: ")
        v = Validators(customer_address_state)
        validated_customer_address_state = v.validate_customer_adress_state()
        return validated_customer_address_state

    @staticmethod
    def get_customer_id():
        customer_id = input("Enter the customer's ID: ")
        v = Validators(customer_id)
        validated_customer_id = v.validate_customer_id()
        return validated_customer_id

    @staticmethod
    def get_appointment_day():
        appointment_day = input("Enter the appointment's day: ")
        v = Validators(appointment_day)
        validated_appointment_day = v.validate_appointment_day()
        return validated_appointment_day

    def get_appointment_duration(self):
        appointment_duration = input("Enter the Appointment's duration (HH:MM-HH:MM): ")
        v = Validators(appointment_duration)
        validated_appointment_duration = v.validate_appointment_duration()
        return validated_appointment_duration
