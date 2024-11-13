# from unittest.mock import patch
#
# from src.user_interaction import search


# def test_search(return_search):
#     with patch('builtins.input', side_effect=[
#         "java, Junior, Полная занятость, RUR, 50_000, 100_000"
#     ]):
#         key_word, name, employment, currency, pay_from, pay_to = input(
#             "Введите информацию через запятую: \n"
#             "ЯП, которым владеете; \n"
#             "ваш уровень пользования этим языком;\n"
#             "форма занятости; \n"
#             "валюта, в которой хотите получать зарплату;\n"
#             "зарплатА ОТ; \n"
#             "зарплата ДО: \n"
#         ).split(", ")
#
#         vacations = search(key_word, name, employment, currency, pay_from, pay_to)
#         assert vacations == return_search
