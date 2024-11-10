import requests

from src.DataFile import DataFile
from src.GetVacancies import GetVacancies


def user_interaction():
    """Функция, взаимодействующая с пользователем через консоль. Возможности этой функции следующие:
    возможность ввести поисковый запрос для запроса вакансий из hh.ru;
    возможность получить топ N вакансий по зарплате (N запрашивать у пользователя);
    возможность получить вакансии с ключевым словом в описании."""

    keyword, name, employment, currency, pay_from, pay_to = input(
        "Введите информацию через запятую: \n"
        "ЯП, которым владеете; \n"
        "ваш уровень пользования этим языком;\n"
        "форма занятости; \n"
        "валюта, в которой хотите получать зарплату;\n"
        "зарплатА ОТ; \n"
        "зарплата ДО: \n"
    ).split(", ")
    data_to_file = DataFile(
        keyword, name, employment, currency, int(pay_from), int(pay_to), "../data/hh_vacancies.json"
    )
    operation_data = data_to_file.save_data()

    vacancies = GetVacancies(keyword).loading()
    list_vacancies = []
    for vacancy in vacancies:
        if (
            vacancy.get("salary") is None
            or vacancy["salary"].get("to") is None
            or vacancy["salary"].get("from") is None
            or vacancy in list_vacancies
        ):
            continue
        list_vacancies.append(vacancy)

    for vacancy in list_vacancies:
        avg_pay = (vacancy["salary"].get("from") + vacancy["salary"].get("to")) / 2
        vacancy["salary"]["avg"] = avg_pay

    top_transactions = sorted(list_vacancies, key=lambda x: x["salary"]["avg"])[:5]

    params = {"text": keyword, "per_page": 100}
    url = "https://api.hh.ru/vacancies"
    json_data = requests.get(url, params=params)
    vacancies = json_data.json().get("items", [])
    return operation_data, top_transactions, vacancies


if __name__ == "__main__":
    print(user_interaction())
