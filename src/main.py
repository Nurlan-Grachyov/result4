from src.DataFile import DataFile
from src.user_interaction import user_interaction

if __name__ == "__main__":
    print(user_interaction())
    data_to_file = DataFile(
        "python", "Junior", "Полная занятость", "RUR", 50_000, 100_000, "../data/hh_vacancies.json"
    )
    print(data_to_file.get_data())
