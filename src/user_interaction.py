from src.DataFile import SaveData
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


def search(keyword, keyword_2, occupation, curr, salary_from, salary_to):
    """Функция, с помощью которой пользователь может ввести поисковый запрос для запроса вакансий из hh.ru"""

    data = OperationsWithVacancies(
        keyword, keyword_2, occupation, curr, int(salary_from), int(salary_to))
    operation_data = data._avg()
    readable_list_vacations = []
    for vacancy in operation_data:
        readable_list_vacations.append(
            {
                "имя вакансии": vacancy["name"],
                "месторасположение": vacancy["area"]["name"],
                "средняя зарплата": vacancy["salary"]["avg"],
                "валюта": vacancy["salary"]["currency"],
                "url": vacancy["alternate_url"],
            }
        )
    return readable_list_vacations


def top_vacations(keyword):
    """Функция, с помощью которой пользователь может получить топ N вакансий по зарплате (N запрашивать у пользователя)"""
    n = int(input('Введите кол-во вакансий с самой высокой зарплатой: '))
    vacancies = GetVacancies(keyword)._loading()
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

    top_five_vacations = sorted(list_vacancies, key=lambda x: x["salary"]["avg"])[:n]
    readable_list_vacations = []
    for vacancy in top_five_vacations:
        readable_list_vacations.append(
            {
                "имя вакансии": vacancy["name"],
                "месторасположение": vacancy["area"]["name"],
                "средняя зарплата": vacancy["salary"]["avg"],
                "валюта": vacancy["salary"]["currency"],
                "url": vacancy["alternate_url"],
            }
        )
    return readable_list_vacations


def get_vacations_with_keyword(keyword):
    """Функция, с помощью которой пользователь может получить вакансии по ключевому слову"""
    vacancies = GetVacancies(keyword)._loading()
    readable_list_vacations = []
    for vacancy in vacancies:
        if (
                vacancy.get("salary") is None
                or vacancy["salary"].get("to") is None
                or vacancy["salary"].get("from") is None
        ):
            continue
        else:
            readable_list_vacations.append(
                {
                    "имя вакансии": vacancy["name"],
                    "месторасположение": vacancy["area"]["name"],
                    "зарплата ОТ": vacancy["salary"]["from"],
                    "зарплата ДО": vacancy["salary"]["to"],
                    "валюта": vacancy["salary"]["currency"],
                    "url": vacancy["alternate_url"],
                }
            )
    return readable_list_vacations


if __name__ == "__main__":
    # print(search(key_word, name, employment, currency, pay_from, pay_to))
    # print(top_vacations(key_word))
    print(get_vacations_with_keyword(key_word))
