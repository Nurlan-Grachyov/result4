from src.DataFile import SaveData
from src.GetVacancies import GetVacancies

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
    """Функция, взаимодействующая с пользователем через консоль. Возможности этой функции следующие:
    возможность ввести поисковый запрос для запроса вакансий из hh.ru;
    возможность получить топ N вакансий по зарплате (N запрашивать у пользователя);
    возможность получить вакансии с ключевым словом в описании."""

    data_to_file = SaveData(
        keyword, keyword_2, occupation, curr, int(salary_from), int(salary_to), "../data/hh_vacancies.json"
    )
    operation_data = data_to_file.save_data()
    return operation_data


def top_vacations(keyword):
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

    top_transactions = sorted(list_vacancies, key=lambda x: x["salary"]["avg"])[:5]
    return top_transactions


def get_vacations_with_keyword(keyword):
    vacancies = GetVacancies(keyword)._loading()
    return vacancies


if __name__ == "__main__":
    print(search(key_word, name, employment, currency, pay_from, pay_to))
    # print(top_vacations(key_word))
    # print(get_vacations_with_keyword(key_word))
