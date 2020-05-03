import sys
import time
from validators.validators import Validators
from data_manager import DataManager as dm


class ConsoleUI():
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
        self.CLASS_SELECTION_SCREEN = 1
        self.action_selection_screen = 2

    def show_menu(self):
        if self.actual_screen == self.CLASS_SELECTION_SCREEN:
            self.select_class()
            self.selected_class = self.validated_user_input
        elif self.actual_screen == self.action_selection_screen:
            self.select_class_action()
            self.selected_class_action = self.validated_user_input
            self.execute_class_action()
        else:
            raise ValueError("Inexisting Screen")


    def get_user_input(self, choose_option_text, valid_options):
        user_input = input(choose_option_text)
        v = Validators(user_input)
        self.validated_user_input = v.validate_selected_input(valid_options, choose_option_text)
        print("")

    def select_class(self):
        self.print_line()
        choose_option_text =  "Select the Database's table:\n" \
                "1 - Appointment\n" \
                "2 - Customer\n" \
                "9 - Exit\n" \
                ""
        valid_options = ["1","2","9"]
        self.get_user_input(choose_option_text, valid_options)
        self.actual_screen += 1

    def select_class_action(self):
        self.print_line()
        appointment_class = "1"
        customer_class = "2"
        exit_app = "9"
        if self.selected_class == appointment_class:
            self.select_appointment_action()
        elif self.selected_class == customer_class:
            self.select_customer_action()
        elif self.selected_class == exit_app:
            print("Goobye!")
            time.sleep(3)
            sys.exit()
        else:
            raise ValueError

    def select_appointment_action(self):
        choose_option_text = \
            "Select the Database's action:\n" \
               "1 - Add new Appointment\n" \
               "2 - Update Appointment\n" \
               "3 - Exclude Appointment\n" \
               "9 - Return\n" \
               ""
        valid_options = ["1","2", "3", "9"]
        self.get_user_input(choose_option_text, valid_options)


    def select_customer_action(self):
        choose_option_text = \
            "Select the Database's action:\n" \
               "1 - Add new Customer\n" \
               "2 - Update Customer\n" \
               "3 - Exclude Customer\n" \
               "9 - Return\n" \
               ""

        valid_options = ["1","2", "3", "9"]
        self.get_user_input(choose_option_text, valid_options)


    def execute_class_action(self):
        self.print_line()
        appointment = "1"
        customer = "2"
        return_screen = "9"
        if self.selected_class_action == return_screen:
            print("Selected Option: Return to the last screen\n\n")
        elif self.selected_class == appointment:
            self.execute_appointment_action()
        elif self.selected_class == customer:
            self.execute_customer_action()
        self.actual_screen = self.CLASS_SELECTION_SCREEN



    def execute_appointment_action(self):
        new_appointment = "1"
        update_appointment = "2"
        exclude_appointment = "3"
        if self.selected_class_action == new_appointment:
            print("Selected Option: Add new Appointment\n\n")
            #add new appointment function

        elif self.selected_class_action == update_appointment:
            print("Selected Option: Update Appointment\n\n")
            #add update appointment function

        elif self.selected_class_action == exclude_appointment:
            print("Selected Option: Exclude Appointment\n\n")
            #add exclude appointment function
        else:
            raise ValueError
        self.actual_screen = self.CLASS_SELECTION_SCREEN

    def execute_customer_action(self):
        new_customer = "1"
        update_customer = "2"
        exclude_customer = "3"
        if self.selected_class_action == new_customer:
            print("Selected Option: Add new Customer\n\n")
            #add new customer function
            self.dm.add_new_customer_to_database()
        elif self.selected_class_action == update_customer:
            print("Selected Option: Update Customer\n\n")
            #add update customer function
        elif self.selected_class_action == exclude_customer:
            print("Selected Option: Exclude Customer\n\n")
            #add exclude customer function
        else:
            raise ValueError
        self.actual_screen = self.CLASS_SELECTION_SCREEN

    def print_line(self):
        print("---------")

if __name__ == "__main__":
    c = ConsoleUI()