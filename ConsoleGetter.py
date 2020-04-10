from Validators import Validators

class ConsoleGetter():

    @staticmethod
    def get_student_forename():
        student_forename = input("Enter the student's student_forename: ")
        Validators().raise_type_error_if_not_string(student_forename)
        validated_student_forename = Validators().validate_alpha_and_spaces_len25(student_forename)
        return validated_student_forename

    @staticmethod
    def get_student_surname():
        student_surname = input("Enter the student's student_surname: ")
        Validators().raise_type_error_if_not_string(student_surname)
        validated_student_surname = Validators().validate_alpha_and_spaces_len25(student_surname)
        return validated_student_surname

    @staticmethod
    def get_student_birthday():
        student_birthday = input("Enter the student's birthname (DD-MM-YYYY): ")
        Validators().raise_type_error_if_not_string(student_birthday)
        return student_birthday

    @staticmethod
    def get_student_id_number():
        student_id_number = input("Enter the student's ID number: ")
        Validators().raise_type_error_if_not_string(student_id_number)
        validated_student_id_number = Validators().validate_id_number(student_id_number)
        return validated_student_id_number

    @staticmethod
    def get_student_adress_street_and_number():
        student_adress_street_and_number = input("Digite a rua e o número do local de residência do estudante: ")
        Validators().raise_type_error_if_not_string(student_adress_street_and_number)
        return student_adress_street_and_number

    @staticmethod
    def get_student_adress_others():
        student_adress_others = input("Digite o apartamento ou outra referência (NA = Não aplica): ")
        Validators().raise_type_error_if_not_string(student_adress_others)
        return student_adress_others

    @staticmethod
    def get_student_adress_city():
        student_adress_city = input("Digite a cidade do estudante: ")
        Validators().raise_type_error_if_not_string(student_adress_city)
        validated_student_adress_city = Validators().validate_alpha_and_spaces_len25(student_adress_city)
        return validated_student_adress_city

    @staticmethod
    def get_student_adress_state():
        student_adress_state = input("Digite o estado do estudante: ")
        Validators().raise_type_error_if_not_string(student_adress_state)
        validated_student_adress_state = Validators().validate_alpha_and_spaces_len25(student_adress_state)
        return validated_student_adress_state
