import json
from abc import abstractmethod, ABC

from src.OperationsWithVacancies import OperationsWithVacancies


class AbstractSave(ABC):
    """Абстрактный класс, который обязывает реализовать метод для добавления вакансий в файл"""

    @abstractmethod
    def save_data(self):
        """Метод для добавления вакансий в файл, который должен быть в дочернем классе"""
        pass


class AbstractGet(ABC):
    """Абстрактный класс, который обязывает реализовать метод для получения данных из файла по указанным критериям"""

    @abstractmethod
    def get_data(self):
        """Метод для получения данных из файла по указанным критериям, который должен быть в дочернем классе"""
        pass


class AbstractDelete(ABC):
    """Абстрактный класс, который обязывает реализовать метод для удаления информации о вакансиях"""

    @abstractmethod
    def delete_data(self):
        """Метод для удаления информации о вакансиях, который должен быть в дочернем классе"""
        pass


class SaveData(OperationsWithVacancies, AbstractSave):
    """Класс для работы с добавления информации о вакансиях в JSON-файл"""

    try:

        def __init__(
            self, keyword, keyword_2, employment, currency, pay_from, pay_to, file="../data/hh_vacancies.json"
        ):  # noqa: E501
            super().__init__(keyword, keyword_2, employment, currency, pay_from, pay_to)
            self.__file = file

        def save_data(self):
            """Метод для добавления вакансий в файл"""
            with open(self.__file, "r", encoding="utf-8") as file:
                try:
                    data_from_json_file = json.load(file)
                except json.decoder.JSONDecodeError:
                    data_from_json_file = []
                for vacancy in self._comparison_pay():
                    if vacancy not in data_from_json_file:
                        data_from_json_file.append(vacancy)

            with open(self.__file, "w", encoding="utf-8") as file:
                json.dump(data_from_json_file, file, ensure_ascii=False)
            return self._comparison_pay()

    except Exception as e:
        print(e)
        print("Ошибка в классе DataFile")


class GetData(OperationsWithVacancies, AbstractGet):
    """Класс для получения информации о вакансиях в JSON-файл"""

    try:

        def __init__(
            self, keyword, keyword_2, employment, currency, pay_from, pay_to, file="../data/hh_vacancies.json"
        ):  # noqa: E501
            super().__init__(keyword, keyword_2, employment, currency, pay_from, pay_to)
            self.__file = file

        def get_data(self):
            """Метод для получения данных из файла по указанным критериям"""
            with open(self.__file, "r", encoding="utf-8") as file:
                try:
                    data_from_json_file = json.load(file)
                except json.decoder.JSONDecodeError:
                    return "Файл пустой"
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

    except Exception as e:
        print(e)
        print("Ошибка в классе DataFile")


class DeleteData(OperationsWithVacancies, AbstractDelete):
    """Класс для очистки JSON-файла"""

    try:

        def __init__(
            self, keyword, keyword_2, employment, currency, pay_from, pay_to, file="../data/hh_vacancies.json"
        ):  # noqa: E501
            super().__init__(keyword, keyword_2, employment, currency, pay_from, pay_to)
            self.__file = file

        def delete_data(self):
            """Метод для удаления информации о вакансиях"""
            with open(self.__file, "w"):
                return f"Файл {self.__file} очищен"

    except Exception as e:
        print(e)
        print("Ошибка в классе DataFile")


if __name__ == "__main__":
    data_to_file = DeleteData(
        "java", "Junior", "Полная занятость", "RUR", 50_000, 100_000, "../data/hh_vacancies.json"
    )
    print(data_to_file.delete_data())
