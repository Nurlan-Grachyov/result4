from typing import Any

from src.GetVacancies import GetVacancies
from src.OperationsWithVacancies import OperationsWithVacancies

key_word, name, employment, currency, pay_from, pay_to = input(
    "Введите информацию через запятую: \n"
    "ЯП, которым владеете; \n"
    "ваш уровень пользования этим языком;\n"
    "форма занятости; \n"
    "валюта, в которой хотите получать зарплату;\n"
    "зарплатА ОТ; \n"
    "зарплата ДО: \n"
).split(", ")


def search(keyword: str, keyword_2: str, occupation: str, curr: str, salary_from: str, salary_to: str) -> Any:
    """Функция, с помощью которой пользователь может ввести поисковый запрос для запроса вакансий из hh.ru"""

    data = OperationsWithVacancies(keyword, keyword_2, occupation, curr, int(salary_from), int(salary_to))
    operation_data = data._avg()
    readable_list_vacations = []
    for post in operation_data:
        readable_list_vacations.append(
            f"Имя вакансии - {post["name"]},"
            f"месторасположение - {post["area"]["name"]},"
            f"средняя зарплата - {post["salary"]["avg"]},"
            f"валюта - {post["salary"]["currency"]},"
            f"url - {post["alternate_url"]}"
        )
    return readable_list_vacations


def top_vacations(keyword: str) -> list:
    """Функция,
    с помощью которой пользователь может получить топ N вакансий по зарплате(N запрашивать у пользователя)"""
    n = int(input("Введите кол-во вакансий с самой высокой зарплатой: "))
    vacancies = GetVacancies(keyword)._loading()
    list_vacancies = []
    for employee in vacancies:
        if (
            employee.get("salary") is None
            or employee["salary"].get("to") is None
            or employee["salary"].get("from") is None
            or employee in list_vacancies
        ):
            continue
        list_vacancies.append(employee)

    for vacation in list_vacancies:
        avg_pay = (vacation["salary"].get("from") + vacation["salary"].get("to")) / 2
        vacation["salary"]["avg"] = avg_pay

    top_five_vacations = sorted(list_vacancies, key=lambda x: x["salary"]["avg"])[:n]
    readable_list_vacations = []
    for job in top_five_vacations:
        readable_list_vacations.append(
            {
                "имя вакансии": job["name"],
                "месторасположение": job["area"]["name"],
                "средняя зарплата": job["salary"]["avg"],
                "валюта": job["salary"]["currency"],
                "url": job["alternate_url"],
            }
        )
    return readable_list_vacations


def get_vacations_with_keyword(keyword: str) -> list:
    """Функция, с помощью которой пользователь может получить вакансии по ключевому слову"""
    vacancies = GetVacancies(keyword)._loading()
    readable_list_vacations = []
    for worker in vacancies:
        if worker.get("salary") is None or worker["salary"].get("to") is None or worker["salary"].get("from") is None:
            continue
        else:
            readable_list_vacations.append(
                {
                    "имя вакансии": worker["name"],
                    "месторасположение": worker["area"]["name"],
                    "зарплата ОТ": worker["salary"]["from"],
                    "зарплата ДО": worker["salary"]["to"],
                    "валюта": worker["salary"]["currency"],
                    "url": worker["alternate_url"],
                }
            )
    return readable_list_vacations


if __name__ == "__main__":
    vacations = search(key_word, name, employment, currency, pay_from, pay_to)
    for vacancy in vacations:
        print(vacancy)
    # print(top_vacations(key_word))
    # print(get_vacations_with_keyword(key_word))
