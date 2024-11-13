from src.DataFile import GetData
from src.user_interaction import (currency, employment, get_vacations_with_keyword, key_word, name, pay_from, pay_to,
                                  search, top_vacations)

if __name__ == "__main__":
    vacations = search(key_word, name, employment, currency, pay_from, pay_to)
    for vacancy in vacations:
        print(vacancy)
    print(top_vacations(key_word))
    print(get_vacations_with_keyword(key_word))
    data_to_file = GetData("python", "Junior", "Полная занятость", "RUR", 50_000, 100_000, "../data/hh_vacancies.json")
    print(data_to_file._get_data())
# java, Junior, Полная занятость, RUR, 50_000, 100_000
# тесты
