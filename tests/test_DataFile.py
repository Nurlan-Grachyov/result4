from src.DataFile import SaveData


def test_save_data(return_test_comparison):
    data = SaveData("java", "Junior", "Полная занятость", "RUR", 50_000, 100_000, "../data/hh_vacancies.json")
    data._save_data()
