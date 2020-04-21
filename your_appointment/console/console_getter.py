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
    def get_student_adress_street_and_number():
        student_adress_street_and_number = input("Enter the street and street number: ")
        Validators().raise_type_error_if_not_string(student_adress_street_and_number)
        return student_adress_street_and_number

    @staticmethod
    def get_student_adress_others():
        student_adress_others = input("Enter other adress information (NA = Not applies): ")
        Validators().raise_type_error_if_not_string(student_adress_others)
        return student_adress_others

    @staticmethod
    def get_student_adress_city():
        student_adress_city = input("Enter the student's city: ")
        Validators().raise_type_error_if_not_string(student_adress_city)
        validated_student_adress_city = Validators().validate_alpha_and_spaces_len25(student_adress_city)
        return validated_student_adress_city

    @staticmethod
    def get_student_adress_state():
        student_adress_state = input("Enter the student's state: ")
        Validators().raise_type_error_if_not_string(student_adress_state)
        validated_student_adress_state = Validators().validate_alpha_and_spaces_len25(student_adress_state)
        return validated_student_adress_state
