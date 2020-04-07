
class Validators():


	@staticmethod
	def validate_string_alpha_and_spaces_len25(string_to_validate:str):
		while not Validators().is_alpha_or_has_spaces(string_to_validate) or len(string_to_validate) > 25:
			while not Validators().is_alpha_or_has_spaces(string_to_validate):
				print("Invalid input. The name muss contain only letter or spaces.")
				string_to_validate = input("Enter the student's name: ")
			while len(string_to_validate) > 20:
				print("Invalid input. The name may not be longer than 25 characters.")
				string_to_validate = input("Enter the student's name: ")

		return string_to_validate

	@staticmethod
	def is_alpha_or_has_spaces(forename):
		return True if forename.replace(" ", "").isalpha() else False