import sys
import time
from validators.validators import Validators
from data_manager import DataManager as dm


class ConsoleUI():

    CLASS_SELECTION_SCREEN = 1
    ACTION_SELECTION_SCREEN = 2
    APPOINTMENT_CLASS = "1"
    CUSTOMER_CLASS = "2"
    EXIT_APP = "9"
    RETURN_SCREEN = "9"

    def __init__(self):
        self.dm = dm()
        self.initialize()

    def initialize(self):
        self.show_welcome_message()
        self.define_screens()
        while True:
            self.show_menu()

    def show_welcome_message(self):
        print("Welcome to YourAppoint - by Germain M. Pereira\n")

    def define_screens(self):
        self.actual_screen = 1

    def show_menu(self):
        if self.actual_screen == self.CLASS_SELECTION_SCREEN:
            self.select_class()
            self.selected_class = self.validated_user_input
        elif self.actual_screen == self.ACTION_SELECTION_SCREEN:
            self.select_class_action()
            self.selected_class_action = self.validated_user_input
            self.execute_class_action()
        else:
            raise ValueError("Inexisting Screen")


    def get_user_input(self, CHOOSE_OPTION_TEXT, VALID_OPTIONS):
        user_input = input(CHOOSE_OPTION_TEXT)
        v = Validators(user_input)
        self.validated_user_input = v.validate_selected_input(VALID_OPTIONS, CHOOSE_OPTION_TEXT)
        print("")

    def select_class(self):
        self.print_line()
        CHOOSE_OPTION_TEXT =  "Select the Database's table:\n" \
                "1 - Appointment\n" \
                "2 - Customer\n" \
                "9 - Exit\n" \
                ""
        VALID_OPTIONS = ["1","2","9"]
        self.get_user_input(CHOOSE_OPTION_TEXT, VALID_OPTIONS)
        self.actual_screen += 1

    def select_class_action(self):
        self.print_line()

        if self.selected_class == APPOINTMENT_CLASS:
            self.select_appointment_action()
        elif self.selected_class == CUSTOMER_CLASS:
            self.select_customer_action()
        elif self.selected_class == EXIT_APP:
            print("Goobye!")
            time.sleep(3)
            sys.exit()
        else:
            raise ValueError

    def select_appointment_action(self):
        CHOOSE_OPTION_TEXT = \
            "Select the Database's action:\n" \
               "1 - Add new Appointment\n" \
               "2 - Update Appointment\n" \
               "3 - Exclude Appointment\n" \
               "9 - Return\n" \
               ""
        VALID_OPTIONS = ["1","2", "3", "9"]
        self.get_user_input(CHOOSE_OPTION_TEXT, VALID_OPTIONS)


    def select_customer_action(self):
        CHOOSE_OPTION_TEXT = \
            "Select the Database's action:\n" \
               "1 - Add new Customer\n" \
               "2 - Update Customer\n" \
               "3 - Exclude Customer\n" \
               "9 - Return\n" \
               ""

        VALID_OPTIONS = ["1","2", "3", "9"]
        self.get_user_input(CHOOSE_OPTION_TEXT, VALID_OPTIONS)


    def execute_class_action(self):
        self.print_line()
        if self.selected_class_action == self.RETURN_SCREEN:
            print("Selected Option: Return to the last screen\n\n")
        elif self.selected_class == self.APPOINTMENT_CLASS:
            self.execute_appointment_action()
        elif self.selected_class == self.CUSTOMER_CLASS:
            self.execute_customer_action()
        self.actual_screen = self.CLASS_SELECTION_SCREEN



    def execute_appointment_action(self):
        NEW_APPOINTMENT = "1"
        UPDATE_APPOINTMENT = "2"
        EXCLUDE_APPOINTMENT = "3"
        if self.selected_class_action == NEW_APPOINTMENT:
            print("Selected Option: Add new Appointment\n\n")
            #add new appointment function

        elif self.selected_class_action == UPDATE_APPOINTMENT:
            print("Selected Option: Update Appointment\n\n")
            #add update appointment function

        elif self.selected_class_action == EXCLUDE_APPOINTMENT:
            print("Selected Option: Exclude Appointment\n\n")
            #add exclude appointment function
        else:
            raise ValueError
        self.actual_screen = self.CLASS_SELECTION_SCREEN

    def execute_customer_action(self):
        NEW_CUSTOMER = "1"
        UPDATE_CUSTOMER = "2"
        EXCLUDE_CUSTOMER = "3"
        if self.selected_class_action == NEW_CUSTOMER:
            print("Selected Option: Add new Customer\n\n")
            #add new customer function
            self.dm.add_NEW_CUSTOMER_to_database()
        elif self.selected_class_action == UPDATE_CUSTOMER:
            print("Selected Option: Update Customer\n\n")
            #add update customer function
        elif self.selected_class_action == EXCLUDE_CUSTOMER:
            print("Selected Option: Exclude Customer\n\n")
            #add exclude customer function
        else:
            raise ValueError
        self.actual_screen = self.CLASS_SELECTION_SCREEN

    def print_line(self):
        print("---------")

if __name__ == "__main__":
    c = ConsoleUI()