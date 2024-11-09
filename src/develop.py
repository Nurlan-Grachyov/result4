from abc import ABC, abstractmethod

import requests

class AbstractGet(ABC):

    @abstractmethod
    def loading(self):
        pass


class AbstractSave(ABC):

    @abstractmethod
    def save_data(self):
        pass

class GetVacancies(AbstractGet):

    def __init__(self, keyword):
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {'text': keyword, 'per_page': 100}
        self.keyword = keyword
        self.vacancies = []

    def loading(self):
        json_data = requests.get(self.url, params=self.params)
        self.vacancies = json_data.json()["items"]
        return self.vacancies

class OperationsWithVacancies(GetVacancies):
    def __init__(self,keyword, name, employment, experience, pay_from, pay_to):
        super().__init__(keyword)
        self.name = [vacancies[name] for vacancies in self.vacancies] #'Junior Developer'
        self.employment = [vacancies[employment] for vacancies in self.vacancies] #'Полная занятость'
        self.experience = [vacancies[experience] for vacancies in self.vacancies] #'От 1 года до 3 лет'
        self.pay_from = [vacancies['salary'][pay_from] for vacancies in self.vacancies]
        self.pay_to = [vacancies['salary'][pay_to] for vacancies in self.vacancies]

data = OperationsWithVacancies('python', 'Junior Developer', 'Полная занятость', 'От 1 года до 3 лет', 50_000, 100_000)
print(data.loading())
