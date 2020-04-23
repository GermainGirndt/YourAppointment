from validators.validators import Validators

class ConsoleGetter():

    @staticmethod
    def get_student_forename():
        student_forename = input("Enter the student's forename: ")
        validated_student_forename = Validators().validate_student_forename(student_forename)
        return validated_student_forename

    @staticmethod
    def get_student_surname():
        student_surname = input("Enter the student's surname: ")
        validated_student_surname = Validators().validate_student_surname(student_surname)
        return validated_student_surname

    @staticmethod
    def get_student_birthday():
        student_birthdate = input("Enter the student's birthday (DD-MM-YYYY): ")
        validated_student_birthday = Validators().validate_student_birthdate(student_birthdate)
        return validated_student_birthday

    @staticmethod
    def get_student_id_number():
        student_id_number = input("Enter the student's ID number: ")
        validated_student_id_number = Validators().validate_id_number(student_id_number)
        return validated_student_id_number

    @staticmethod
    def get_student_address_street_and_number():
        student_address_street_and_number = input("Enter the student's street and street number: ")
        validated_student_address_street_and_number = Validators().validate_student_address_street_and_number(student_address_street_and_number)
        return validated_student_address_street_and_number

    @staticmethod
    def get_student_address_others():
        student_address_others = input("Enter other address information (NA = Not applies): ")
        validated_student_address_others = Validators().validate_student_address_others(
            student_address_others)
        return validated_student_address_others

    @staticmethod
    def get_student_address_city():
        student_address_city = input("Enter the student's city: ")
        Validators().raise_type_error_if_not_string(student_address_city)
        validated_student_address_city = Validators().validate_student_adress_city(student_address_city)
        return validated_student_address_city

    @staticmethod
    def get_student_address_state():
        student_address_state = input("Enter the student's state: ")
        Validators().raise_type_error_if_not_string(student_address_state)
        validated_student_address_state = Validators().validate_alpha_and_spaces_len25(student_address_state)
        return validated_student_address_state
