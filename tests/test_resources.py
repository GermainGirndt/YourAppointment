import unittest
from datetime import datetime

class CommonTestingResources(unittest.TestCase):

    customer_register_day = datetime.now().strftime("%Y-%m-%d")
    customer_register_time = datetime.now().strftime("%H:%M")

    customer_class = "2"


    RIGHT_INPUTS_CUSTOMER_ID_1 = ["João", "da Silva", "23-05-1978",
                                  "297.586.890-10", "Rua Bom Sucesso, 487",
                                  "Casa", "São Paulo", "SP"]

    RIGHT_RETURN_CUSTOMER_ID_1 = ["João", "da Silva", "1978-05-23",
                                  "297.586.890-10", "Rua Bom Sucesso, 487",
                                  "Casa", "São Paulo", "SP",
                                  customer_register_day, customer_register_time, "Active"]

    RIGHT_INPUTS_CUSTOMER_ID_2 = ["Joana", "Silveira", "17-02-1972",
                                  "434.763.780-20", "Felicidade, 14", "Ap. 201",
                                 "Rio de Janeiro", "RJ"]


    RIGHT_RETURN_CUSTOMER_ID_2 = ["Joana", "Silveira", "1972-02-17",
                                  "434.763.780-20", "Felicidade, 14", "Ap. 201",
                                 "Rio de Janeiro", "RJ",
                                  customer_register_day, customer_register_time, "Active"]