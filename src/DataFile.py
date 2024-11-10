import json
from abc import abstractmethod, ABC

from src.OperationsWithVacancies import OperationsWithVacancies


class AbstractFile(ABC):
    """Абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл,
    получения данных из файла по указанным критериям и удаления информации о вакансиях"""

    @abstractmethod
    def save_data(self):
        """Метод для добавления вакансий в файл, который должен быть в дочернем классе"""
        pass

    @abstractmethod
    def get_data(self):
        """Метод для получения данных из файла по указанным критериям, который должен быть в дочернем классе"""
        pass

    @abstractmethod
    def delete_data(self):
        """Метод для удаления информации о вакансиях, который должен быть в дочернем классе"""
        pass


class DataFile(OperationsWithVacancies, AbstractFile):
    """Класс для работы с информацией о вакансиях в JSON-файл"""

    try:

        def __init__(self, keyword, keyword_2, employment, currency, pay_from, pay_to, file):
            super().__init__(keyword, keyword_2, employment, currency, pay_from, pay_to)
            self.file = file

        def save_data(self):
            """Метод для добавления вакансий в файл"""

            with open(self.file, "w", encoding="utf-8") as file:
                json.dump(self._comparison_pay(), file, ensure_ascii=False)
            return self._comparison_pay()

        def get_data(self):
            """Метод для получения данных из файла по указанным критериям"""
            with open(self.file, "r", encoding="utf-8") as file:
                data_from_json_file = json.load(file)
                for vacancy in data_from_json_file:
                    if (
                        self.keyword_2 in vacancy.get("name")
                        and self.employment in vacancy["employment"].get("name")
                        and self.currency in vacancy["salary"].get("currency")
                        and vacancy["salary"].get("from", 0) >= self.pay_from
                        and vacancy["salary"].get("to", 0) <= self.pay_to
                    ):
                        return data_from_json_file
                    else:
                        continue

        def delete_data(self):
            """Метод для удаления информации о вакансиях"""
            with open(self.file, "w"):
                return f"Файл {self.file} очищен"

    except Exception as e:
        print(e)
        print("Ошибка в классе DataFile")


if __name__ == "__main__":
    data_to_file = DataFile(
        "python", "Junior", "Полная занятость", "RUR", 50_000, 100_000, "../data/hh_vacancies.json"
    )
    print(data_to_file.get_data())
