from abc import ABC, abstractmethod

import requests
import json


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

class OperationWithVacancies(GetVacancies):
    def __init__(self,keyword, name, employment, experience, vacancies_url):
        super().__init__(keyword)
        self.name = [vacancies[name] for vacancies in self.vacancies] #'Junior Developer'
        self.employment = [vacancies[employment] for vacancies in self.vacancies] #'Полная занятость'
        self.experience = [vacancies[experience] for vacancies in self.vacancies] #'От 1 года до 3 лет'
        self.vacancies_url = [vacancies[vacancies_url] for vacancies in self.vacancies] #'https://api.hh.ru/vacancies?employer_id=5031522'

data = OperationWithVacancies('python', 'Junior Developer', 'Полная занятость', 'От 1 года до 3 лет', 'https://api.hh.ru/vacancies?employer_id=5031522')
print(data.loading())
