import pytest

from src.user_interaction import search, top_vacations, get_vacations_with_keyword


@pytest.mark.parametrize(
    "keyword, keyword_2, emp, curr, pey_from, pray_to, expected_output",
    [
        (
            "java",
            "Junior",
            "Полная занятость",
            "RUR",
            "50_000",
            "100_000",
            [
                "Имя вакансии - Junior Java разработчик,месторасположение - Москва,"
                "средняя зарплата - 80000.0,валюта - RUR,url - https://hh.ru/vacancy/109788485",
                "Имя вакансии - Junior Java Developer,месторасположение - Москва,"
                "средняя зарплата - 60000.0,валюта - RUR,url - https://hh.ru/vacancy/110429201",
            ],
        ),
    ],
)
def test_search(keyword, keyword_2, emp, curr, pey_from, pray_to, expected_output):
    assert search(keyword, keyword_2, emp, curr, pey_from, pray_to) == expected_output


@pytest.mark.parametrize(
    "keyword, quantity, expected_output",
    [
        (
            "java",
            "2",
            [
                {
                    "имя вакансии": "Начинающий (Junior) Программист/Стажер",
                    "месторасположение": "Москва",
                    "средняя зарплата": 40000.0,
                    "валюта": "RUR",
                    "url": "https://hh.ru/vacancy/110365805",
                },
                {
                    "имя вакансии": "Программист",
                    "месторасположение": "Ростов-на-Дону",
                    "средняя зарплата": 40500.0,
                    "валюта": "RUR",
                    "url": "https://hh.ru/vacancy/110858048",
                },
            ],
        )
    ],
)
def test_top_vacancies(keyword, quantity, expected_output):
    assert top_vacations(keyword, quantity) == expected_output


# @pytest.mark.parametrize(
#     "keyword, expected_output",
#     [
#         (
#             "java",
#             [
#                 {
#                     "имя вакансии": "Начинающий (Junior) Программист/Стажер",
#                     "месторасположение": "Москва",
#                     "зарплата ОТ": 40000,
#                     "зарплата ДО": 40000,
#                     "валюта": "RUR",
#                     "url": "https://hh.ru/vacancy/110365805",
#                 },
#                 {
#                     "имя вакансии": "Программист",
#                     "месторасположение": "Ростов-на-Дону",
#                     "зарплата ОТ": 35000,
#                     "зарплата ДО": 46000,
#                     "валюта": "RUR",
#                     "url": "https://hh.ru/vacancy/110858048",
#                 },
#                 {
#                     "имя вакансии": "Junior Java разработчик",
#                     "месторасположение": "Москва",
#                     "зарплата ОТ": 60000,
#                     "зарплата ДО": 100000,
#                     "валюта": "RUR",
#                     "url": "https://hh.ru/vacancy/109788485",
#                 },
#                 {
#                     "имя вакансии": "Тестировщик QA/AQA (middle, senior, удалённо)",
#                     "месторасположение": "Москва",
#                     "зарплата ОТ": 80000,
#                     "зарплата ДО": 250000,
#                     "валюта": "RUR",
#                     "url": "https://hh.ru/vacancy/110336167",
#                 },
#                 {
#                     "имя вакансии": "Junior Java Developer",
#                     "месторасположение": "Москва",
#                     "зарплата ОТ": 50000,
#                     "зарплата ДО": 70000,
#                     "валюта": "RUR",
#                     "url": "https://hh.ru/vacancy/110429201",
#                 },
#                 {
#                     "имя вакансии": "Java-разработчик",
#                     "месторасположение": "Иннополис",
#                     "зарплата ОТ": 80000,
#                     "зарплата ДО": 160000,
#                     "валюта": "RUR",
#                     "url": "https://hh.ru/vacancy/110826567",
#                 },
#                 {
#                     "имя вакансии": "HTML-верстальщик/Контент-менеджер сайта",
#                     "месторасположение": "Санкт-Петербург",
#                     "зарплата ОТ": 40000,
#                     "зарплата ДО": 70000,
#                     "валюта": "RUR",
#                     "url": "https://hh.ru/vacancy/110655536",
#                 },
#                 {
#                     "имя вакансии": "Специалист по IT в компанию DYN-IT.DE - стажёр",
#                     "месторасположение": "Астана",
#                     "зарплата ОТ": 260000,
#                     "зарплата ДО": 625000,
#                     "валюта": "KZT",
#                     "url": "https://hh.ru/vacancy/110690816",
#                 },
#                 {
#                     "имя вакансии": "Java/Kotlin разработчик (Java/Kotlin Developer)",
#                     "месторасположение": "Москва",
#                     "зарплата ОТ": 150000,
#                     "зарплата ДО": 300000,
#                     "валюта": "RUR",
#                     "url": "https://hh.ru/vacancy/110619836",
#                 },
#                 {
#                     "имя вакансии": "Тестировщик",
#                     "месторасположение": "Москва",
#                     "зарплата ОТ": 70000,
#                     "зарплата ДО": 100000,
#                     "валюта": "RUR",
#                     "url": "https://hh.ru/vacancy/109478645",
#                 },
#                 {
#                     "имя вакансии": "Младший Java разработчик",
#                     "месторасположение": "Москва",
#                     "зарплата ОТ": 80000,
#                     "зарплата ДО": 100000,
#                     "валюта": "RUR",
#                     "url": "https://hh.ru/vacancy/110669933",
#                 },
#             ],
#         )
#     ],
# )
# def test_get_vacations_with_keyword(keyword, expected_output):
#     assert get_vacations_with_keyword(keyword) == expected_output
