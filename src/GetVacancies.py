from abc import ABC, abstractmethod
import requests


class AbstractGet(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def _loading(self):
        """Метод, который должен быть в дочернем классе"""
        pass


class GetVacancies(AbstractGet):
    """Класс, наследующийся от абстрактного класса, для работы с платформой hh.ru"""

    def __init__(self, keyword):
        """Класс-конструктор, который получает ключевое слово для поиска(keyword)"""
        self.__url = "https://api.hh.ru/vacancies"
        self.__params = {"text": keyword, "per_page": 100}
        self._vacancies = []

    def _loading(self):
        """Метод, подключающийся к API и получающий вакансии"""
        try:
            json_data = requests.get(self.__url, params=self.__params)
            if json_data.status_code == 200:
                self._vacancies = json_data.json().get("items", [])
            return self._vacancies
        except Exception as e:
            print(e)
            print("Ошибка в классе GetVacancies")


if __name__ == "__main__":
    data = GetVacancies("python")
    result = data._loading()
    print(result)
