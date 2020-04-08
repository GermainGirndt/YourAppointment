import datetime





def validate(date_to_validate):
	while True:
		try:
			validated_date = datetime.datetime.strptime(date_to_validate, '%d-%m-%Y')
		except:
			print("Invalid input. The birthdate muss comply to the required format")
			date_to_validate = input("Enter the student's birthname (DD-MM-YYYY): ")
		else:
			return validated_date

lala = input("kaka")
print(validate(lala))