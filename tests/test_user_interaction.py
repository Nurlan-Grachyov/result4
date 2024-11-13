# from unittest.mock import patch
#
# from src.user_interaction import search, key_word, name, employment, currency, pay_from, pay_to
#
# def test_search(return_search):
#     with patch('builtins.input', side_effect=[
#         "java, Junior, Полная занятость, RUR, 50_000, 100_000"
#     ]):
#         vacations = search(key_word, name, employment, currency, pay_from, pay_to)
#         assert vacations == return_search

import unittest
from unittest.mock import patch
from src.user_interaction import search
from src.OperationsWithVacancies import SalaryOfVacancies


class TestSearchFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        "java, Junior, Полная занятость, RUR, 50000, 100000"
    ])
    def test_search(self, mock_input):
        mock_salary_of_vacancies = SalaryOfVacancies("java", "Junior", "Полная занятость", "RUR", 50000, 100000)
        mock_salary_of_vacancies._avg = lambda: [
            {
                "name": "Вакансия 1",
                "area": {"name": "Москва"},
                "salary": {"avg": 75000, "currency": "RUR"},
                "alternate_url": "http://example.com/vacancy1"
            },
            {
                "name": "Вакансия 2",
                "area": {"name": "Санкт-Петербург"},
                "salary": {"avg": 65000, "currency": "RUR"},
                "alternate_url": "http://example.com/vacancy2"
            }
        ]

        vacations = search("java", "Junior", "Полная занятость", "RUR", "50000", "100000")

        expected_result = [
            "Имя вакансии - Вакансия 1,месторасположение - Москва,средняя зарплата - 75000,валюта - RUR,url - http://example.com/vacancy1",
            "Имя вакансии - Вакансия 2,месторасположение - Санкт-Петербург,средняя зарплата - 65000,валюта - RUR,url - http://example.com/vacancy2",
        ]

        self.assertEqual(vacations, expected_result)

if __name__ == '__main__':
    unittest.main()