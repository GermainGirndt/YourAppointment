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
    def validate_alpha_and_spaces_len25(string_to_validate):
        while not Validators().is_alpha_or_has_spaces(string_to_validate) or len(string_to_validate) > 25:
            while not Validators().is_alpha_or_has_spaces(string_to_validate):
                print("Invalid input. The name muss contain only letter or spaces.")
                string_to_validate = input("Enter the student's name: ")
            while len(string_to_validate) > 20:
                print("Invalid input. The name may not be longer than 25 characters.")
                string_to_validate = input("Enter the student's name: ")
        Validators().raise_type_error_if_not_string(string_to_validate)
        return string_to_validate

    @staticmethod
    def is_alpha_or_has_spaces(string_to_validate):
        return True if string_to_validate.replace(" ", "").isalpha() else False

    @staticmethod
    def validate_birthday(date_to_validate):
        while True:
            try:
                validated_date = datetime.datetime.strptime(date_to_validate, '%d-%m-%Y')
            except:
                print("Invalid input. The birthdate muss comply to the required format")
                date_to_validate = input("Enter the student's birthname (DD-MM-YYYY): ")
            else:
                Validators().raise_type_error_if_not_string(date_to_validate)
                return date_to_validate #validated_date would be a datatime object

    @staticmethod
    def validate_id_number(id_number_to_validate):
        while len(id_number_to_validate.replace("-","").replace(".","")) != 11 or not id_number_to_validate.replace("-","").replace(".","").isnumeric():
            while len(id_number_to_validate.replace("-","").replace(".","")) != 11:
                print(f"Invalid input. The id number muss have 11 digits and should have comply to the required format")
                id_number_to_validate = input("Enter the student's birthname (DD-MM-YYYY): ")
            while not id_number_to_validate.replace("-","").replace(".","").isnumeric():
                print(f"Invalid input. The id number may only have numbers, points and dashes")
                id_number_to_validate = input("Enter the student's birthname (DD-MM-YYYY): ")
        return id_number_to_validate