from src.DataFile import GetData
from src.user_interaction import search, top_vacations, get_vacations_with_keyword, key_word, employment, name, \
    currency, pay_from, pay_to

if __name__ == "__main__":
    print(search(key_word, name, employment, currency, pay_from, pay_to))
    print(top_vacations(key_word))
    print(get_vacations_with_keyword(key_word))
    data_to_file = GetData(
        "python", "Junior", "Полная занятость", "RUR", 50_000, 100_000, "../data/hh_vacancies.json"
    )
    print(data_to_file.get_data())
# java, Junior, Полная занятость, RUR, 50_000, 100_000
# типизация, последний критерий 3го задания, тесты, читабельные вакансии