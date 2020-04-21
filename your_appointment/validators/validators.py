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
    def validate_alpha_and_spaces_len25(string_to_validate):
        checks = 0
        while checks < 2:
            while not Validators().is_alpha_or_has_spaces(string_to_validate):
                checks = 0
                print("Invalid input. The name muss contain only letter or spaces.")
                string_to_validate = input("Enter the student's name: ")
            checks += 1
            while len(string_to_validate) > 20:
                checks = 0
                print("Invalid input. The name may not be longer than 25 characters.")
                string_to_validate = input("Enter the student's name: ")
            checks += 1
        Validators().raise_type_error_if_not_string(string_to_validate)
        return string_to_validate

    @staticmethod
    def validate_student_forename(student_forename_to_validate):
        Validators().raise_type_error_if_not_string(student_forename_to_validate)
        checks = 0
        while checks < 2:
            while not Validators().is_alpha_or_has_spaces(student_forename_to_validate):
                checks = 0
                print("Invalid input. The forename muss contain only letters or spaces.")
                student_forename_to_validate = input("Enter the student's forename: ")
                Validators().raise_type_error_if_not_string(student_forename_to_validate)
            checks += 1
            while len(student_forename_to_validate) > 20:
                checks = 0
                print("Invalid input. The forename may not be longer than 25 characters.")
                student_forename_to_validate = input("Enter the student's forename: ")
                Validators().raise_type_error_if_not_string(student_forename_to_validate)
            checks += 1
        Validators().raise_type_error_if_not_string(student_forename_to_validate)
        return student_forename_to_validate


    @staticmethod
    def validate_student_surname(student_surname_to_validate):
        Validators().raise_type_error_if_not_string(student_surname_to_validate)
        checks = 0
        while checks < 2:
            while not Validators().is_alpha_or_has_spaces(student_surname_to_validate):
                checks = 0
                print("Invalid input. The surname muss contain only letters or spaces.")
                student_surname_to_validate = input("Enter the student's surname: ")
                Validators().raise_type_error_if_not_string(student_surname_to_validate)
            checks += 1
            while len(student_surname_to_validate) > 20:
                checks = 0
                print("Invalid input. The surname may not be longer than 25 characters.")
                student_surname_to_validate = input("Enter the student's surname: ")
                Validators().raise_type_error_if_not_string(student_surname_to_validate)
            checks += 1
        return student_surname_to_validate

    @staticmethod
    def validate_birthday(date_to_validate):
        Validators().raise_type_error_if_not_string(date_to_validate)
        while True:
            try:
                datetime.datetime.strptime(date_to_validate, '%d-%m-%Y')
            except ValueError:
                print("Invalid input. The birthdate muss comply to the required format")
                date_to_validate = input("Enter the student's birthday (DD-MM-YYYY): ")
                Validators().raise_type_error_if_not_string(date_to_validate)
            else:
                return date_to_validate #noy using validated_date because it would be a datatime object

    @staticmethod
    def validate_id_number(id_number_to_validate):
        Validators().raise_type_error_if_not_string(id_number_to_validate)
        checks = 2
        while checks < 2:
            while len(id_number_to_validate.replace("-","").replace(".","")) != 11:
                checks = 0
                print(f"Invalid input. The id number muss have 11 digits and should have comply to the required format")
                id_number_to_validate = input("Enter the student's birthname (DD-MM-YYYY): ")
                Validators().raise_type_error_if_not_string(id_number_to_validate)
            checks += 1
            while not id_number_to_validate.replace("-","").replace(".","").isnumeric():
                checks = 0
                print(f"Invalid input. The id number may only have numbers, points and dashes")
                id_number_to_validate = input("Enter the student's birthname (DD-MM-YYYY): ")
                Validators().raise_type_error_if_not_string(id_number_to_validate)
            checks += 1
        return id_number_to_validate