from typing import List

import pytest

from src.user_interaction import search, top_vacations


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
def test_search(
    keyword: str, keyword_2: str, emp: str, curr: str, pey_from: str, pray_to: str, expected_output: List
) -> None:
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
def test_top_vacancies(keyword: str, quantity: str, expected_output: List) -> None:
    assert top_vacations(keyword, quantity) == expected_output
