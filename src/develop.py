import json
from abc import ABC, abstractmethod

import requests


class AbstractGet(ABC):

    @abstractmethod
    def loading(self):
        pass


class AbstractFile(ABC):

    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def delete_data(self):
        pass

class GetVacancies(AbstractGet):

    def __init__(self, keyword):
        self.url = "https://api.hh.ru/vacancies"
        self.params = {"text": keyword, "per_page": 100}
        self.keyword = keyword
        self.vacancies = []

    def loading(self):
        json_data = requests.get(self.url, params=self.params)
        self.vacancies = json_data.json().get("items", [])
        return self.vacancies


class OperationsWithVacancies(GetVacancies):
    def __init__(self, keyword, name, employment, currency, pay_from, pay_to):
        super().__init__(keyword)
        self.loading()
        self.name = name
        self.employment = employment
        self.currency = currency
        self.pay_from = pay_from
        self.pay_to = pay_to
        self.sorted_vacancies = []

    def filtered_vacancies(self):
        for vacancy in self.vacancies:
            if vacancy.get("salary") is None or vacancy["salary"].get("to") is None:
                continue
            if (
                self.name in vacancy.get("name")
                and self.employment in vacancy["employment"].get("name")
                and self.currency in vacancy["salary"].get("currency")
                and vacancy["salary"].get("from", 0) >= self.pay_from
                and vacancy["salary"].get("to", 0) <= self.pay_to
            ):
                print(vacancy)
                self.sorted_vacancies.append(vacancy)
            else:
                continue

        for vacancy in self.sorted_vacancies:
            avg_pay = (vacancy["salary"].get("from") + vacancy["salary"].get("to")) / 2
            vacancy["salary"]["avg"] = avg_pay

        return self.sorted_vacancies

    def comparison_pay(self):
        self.filtered_vacancies()
        if not self.sorted_vacancies:
            return None
        return sorted(self.sorted_vacancies, key=lambda x: x["salary"]["avg"], reverse=True)

    def highest_pay(self):
        self.filtered_vacancies()
        if not self.sorted_vacancies:
            return None
        return max(self.sorted_vacancies, key=lambda x: x["salary"]["avg"])

    def lowest_pay(self):
        self.filtered_vacancies()
        if not self.sorted_vacancies:
            return None
        return min(self.sorted_vacancies, key=lambda x: x["salary"]["avg"])


# class DataFile(AbstractFile):  # Remove OperationsWithVacancies from inheritance
#     def __init__(self, keyword, name, employment, currency, pay_from, pay_to, file):
#         self.operations = OperationsWithVacancies(keyword, name, employment, currency, pay_from, pay_to)
#         self.comparison_pay = self.operations.comparison_pay()
#         self.file = file
#
#     def save_data(self):
#         with open(self.file, "w") as file:
#             # json.dump(self.comparison_pay, file)
#             json.dump(self.operations.sorted_vacancies, file)
#         return self.operations.sorted_vacancies
#
#     def get_data(self):
#         # with open(self.file, "r") as file:
#         #     return json.load(file)
#         pass
#     def delete_data(self):
#         pass

class DataFile(OperationsWithVacancies, AbstractFile):  # Remove OperationsWithVacancies from inheritance
    def __init__(self, keyword, name, employment, currency, pay_from, pay_to, file):
        super().__init__(keyword, name, employment, currency, pay_from, pay_to)
        self.file = file

    def save_data(self):
        with open(self.file, "w") as file:
            json.dump(self.comparison_pay(), file)
            print(self.comparison_pay())
        return self.comparison_pay()

    def get_data(self):
        # with open(self.file, "r") as file:
        #     return json.load(file)
        pass
    def delete_data(self):
        pass
if __name__ == '__main__':
    # data = GetVacancies("python")
    # # sorted_data = OperationsWithVacancies("python", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    # print(sorted_data.filtered_vacancies())
    # print(sorted_data.lowest_pay())
    data_to_file = DataFile("python", "Junior", "Полная занятость", "RUR", 50_000, 100_000, "../data/hh_vacancies.json")
    save_data = data_to_file.save_data()