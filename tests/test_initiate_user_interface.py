import set_test_path
import unittest
from data_manager import DataManager
from data_manager import Database
import sqlite3
import os
from datetime import datetime
from unittest import mock
from testing_resources import TestingShortcuts
from io import StringIO
from app import ConsoleUI
from contextlib import redirect_stdout

class TestUserInterface(TestingShortcuts, unittest.TestCase):

    #General
    APPOINTMENT_CLASS = "1"
    CUSTOMER_CLASS = "2"
    EXIT_APP = "9"
    RETURN_SCREEN = "9"
    #Customer class
    CREATE_CUSTOMER = "1"
    READ_CUSTOMER = "2"
    EXCLUDE_CUSTOMER = "3"
    #Appointment class
    CREATE_APPOINTMENT = "1"
    READ_APPOINTMENT = "2"
    EXCLUDE_APPOINTMENT = "3"

    INPUTS_SELECT_ACTION_CREATE_CUSTOMER = [CUSTOMER_CLASS, CREATE_CUSTOMER]
    INPUTS_SELECT_ACTION_READ_CUSTOMER = [CUSTOMER_CLASS, READ_CUSTOMER]
    INPUTS_SELECT_ACTION_EXCLUDE_CUSTOMER = [CUSTOMER_CLASS, EXCLUDE_CUSTOMER]

    INPUTS_SELECT_ACTION_CREATE_APPOINTMENT = [APPOINTMENT_CLASS, CREATE_APPOINTMENT]

    def setUp(self):
        db_file = "YourAppointment.db"
        if os.path.exists(db_file):
            os.remove(db_file)
        self.dm = DataManager()
        with redirect_stdout(StringIO()) as stdout:
            self.dm.db.create_table_customers()
        self.console_ui = ConsoleUI()

    def test_execute_customer_action_create_customer(self):
        create_customer_id_1_inputs = self.INPUTS_SELECT_ACTION_CREATE_CUSTOMER + self.RIGHT_INPUTS_CUSTOMER_ID_1
        self.shortcut_test_console_ui_inputs(
            inputs=create_customer_id_1_inputs,
            testing_function=self.shortcut_console_ui_test_if_customer_in_db_by_id,
            parameter=(self.DB_RIGHT_RETURN_CUSTOMER_ID_1)
        )

    def test_execute_customer_action_create_2_customers(self):
        self.test_execute_customer_action_create_customer()
        create_customer_id_2_inputs = self.INPUTS_SELECT_ACTION_CREATE_CUSTOMER + self.RIGHT_INPUTS_CUSTOMER_ID_2
        self.shortcut_test_console_ui_inputs(
            inputs=create_customer_id_2_inputs,
            testing_function=self.shortcut_console_ui_test_if_customer_in_db_by_id,
            parameter=(self.DB_RIGHT_RETURN_CUSTOMER_ID_2)
        )

    def test_execute_customer_action_read_customer_by_name(self):
        self.test_execute_customer_action_create_customer()
        customer_id_1_name = "João"
        read_customer_inputs = self.INPUTS_SELECT_ACTION_READ_CUSTOMER + [customer_id_1_name]
        expected_message = f"{self.DB_RIGHT_RETURN_CUSTOMER_ID_1}"
        self.shortcut_test_console_ui_inputs(
            inputs=read_customer_inputs,
            testing_function=self.shortcut_test_if_expected_message_in_console_stdoutput,
            parameter=expected_message,
            use_printed_messages=True
        )

    def test_execute_customer_action_exclude_by_id(self):
        self.test_execute_customer_action_create_customer()
        customer_id_1_id = "1"
        read_customer_inputs = self.INPUTS_SELECT_ACTION_EXCLUDE_CUSTOMER + [customer_id_1_id]
        expectedOutput = self.shortcut_set_customer_to_inactive(self.DB_RIGHT_RETURN_CUSTOMER_ID_1)
        self.shortcut_test_console_ui_inputs(
            inputs=read_customer_inputs,
            testing_function=self.shortcut_console_ui_test_if_customer_in_db_by_id,
            parameter=expectedOutput
        )


    def test_execute_appointment_action_create_appointment(self):
        self.test_execute_customer_action_create_customer()
        create_appointment_inputs = self.INPUTS_SELECT_ACTION_CREATE_APPOINTMENT + self.RIGHT_INPUTS_APPOINTMENT_ID_1_OF_CUSTOMER_ID_1

        self.shortcut_test_console_ui_inputs(
            inputs=create_appointment_inputs,
            testing_function=self.shortcut_test_if_expected_message_in_console_stdoutput,
            parameter=str(self.DB_RIGHT_RETURN_APPOINTMENT_ID_1_OF_CUSTOMER_ID_1),
            use_printed_messages=True
        )

if __name__ == "__main__":
    unittest.main()