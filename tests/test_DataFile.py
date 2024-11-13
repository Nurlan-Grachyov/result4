from typing import List

from src.DataFile import DeleteData, GetData, SaveData


def test_save_data(return_save_data: List) -> None:
    save_data = SaveData("java", "Junior", "Полная занятость", "RUR", 50_000, 100_000, "../data/hh_vacancies.json")
    assert save_data._save_data() == return_save_data
    # get_data = GetData("java", "Junior", "Полная занятость", "RUR", 50_000, 100_000, "../data/hh_vacancies.json")

    del_data = DeleteData("java", "Junior", "Полная занятость", "RUR", 50_000, 100_000, "../data/hh_vacancies.json")
    assert del_data._keyword == "java"
    assert del_data._keyword_2 == "Junior"
    assert del_data._employment == "Полная занятость"
    assert del_data._currency == "RUR"
    assert del_data._pay_from == 50_000
    assert del_data._pay_to == 100_000
