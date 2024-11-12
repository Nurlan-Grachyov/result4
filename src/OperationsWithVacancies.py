from abc import ABC, abstractmethod
from typing import Any, List

from src.GetVacancies import GetVacancies


class AbstractOperation(ABC):
    """Абстрактный класс для работы с полученными вакансиями"""

    @abstractmethod
    def _filtered_vacancies(self):
        """Метод, который должен быть в дочернем классе"""
        pass


class AbstractSalary(ABC):
    """Абстрактный класс для получения средней зарплаты в полученных вакансиях"""

    @abstractmethod
    def _avg(self):
        """Метод, который должен быть в дочернем классе"""
        pass


class OperationsWithVacancies(GetVacancies):
    """Класс для работы с вакансиями"""

    __slots__ = ("keyword", "keyword_2", "employment", "currency", "pay_from", "pay_to")

    def __init__(self, keyword: str, keyword_2: str, employment: str, currency: str, pay_from: int, pay_to: int):
        """Класс-конструктор, который получает атрибуты"""
        super().__init__(keyword)
        self._loading()
        self.keyword_2 = keyword_2
        self.employment = employment
        self.currency = currency
        if pay_from < 0:
            raise ValueError("Зарплата ОТ не должна быть отрицательной")
        self.pay_from = pay_from
        if pay_to < pay_from:
            raise ValueError("Зарплата ДО не должна быть меньше зарплаты ОТ")
        self.pay_to = pay_to
        self.sorted_vacancies: List = []

    def _filtered_vacancies(self) -> list:
        """Метод, фильтрует вакансии по фильтрам"""
        try:
            for vacancy in self._vacancies:
                if (
                    vacancy.get("salary") is None
                    or vacancy["salary"].get("to") is None
                    or vacancy["salary"].get("from") is None
                    or vacancy in self.sorted_vacancies
                ):
                    continue
                elif (
                    self.keyword_2 in vacancy.get("name")
                    and self.employment in vacancy["employment"].get("name")
                    and self.currency in vacancy["salary"].get("currency")
                    and vacancy["salary"].get("from", 0) >= self.pay_from
                    and vacancy["salary"].get("to", 0) <= self.pay_to
                ):
                    self.sorted_vacancies.append(vacancy)
                else:
                    continue
            return self.sorted_vacancies

        except Exception as e:
            print(e)
            print("Ошибка в классе OperationsWithVacancies")
            return []


class SalaryOfVacancies(OperationsWithVacancies):
    """Класс, работающий с зарплатами вакансий"""

    def _avg(self) -> list:
        """Метод, высчитывающий среднюю зарплату для каждой вакансии"""
        self._filtered_vacancies()
        for vacancy in self.sorted_vacancies:
            avg_pay = (vacancy["salary"].get("from") + vacancy["salary"].get("to")) / 2
            vacancy["salary"]["avg"] = avg_pay
        return self.sorted_vacancies

    def _comparison_pay(self) -> None | list:
        """Метод, сортирующий вакансии со средними зарплатами в порядке возрастания"""
        self._avg()
        if not self.sorted_vacancies:
            return None
        return sorted(self.sorted_vacancies, key=lambda x: x["salary"]["avg"], reverse=True)

    def _highest_pay(self) -> Any:
        """Метод, возвращающий вакансию с максимальной средней зарплатой"""
        self._avg()
        if not self.sorted_vacancies:
            return None
        return max(self.sorted_vacancies, key=lambda x: x["salary"]["avg"])

    def _lowest_pay(self) -> Any:
        """Метод, возвращающий вакансию с минимальной средней зарплатой"""
        self._avg()
        if not self.sorted_vacancies:
            return None
        return min(self.sorted_vacancies, key=lambda x: x["salary"]["avg"])

    def _get_max_avg_salary(self) -> float:
        """Метод возвращает максимальную среднюю зарплату в списке вакансий"""
        self._avg()
        highest_vacancy = self._highest_pay()
        return highest_vacancy["salary"]["avg"] if highest_vacancy else 0

    def __eq__(self, other: Any) -> Any:
        return self._get_max_avg_salary() == other._get_max_avg_salary()

    def __lt__(self, other: Any) -> Any:
        return self._get_max_avg_salary() < other._get_max_avg_salary()

    def __le__(self, other: Any) -> Any:
        return self._get_max_avg_salary() <= other._get_max_avg_salary()

    def __gt__(self, other: Any) -> Any:
        return self._get_max_avg_salary() > other._get_max_avg_salary()

    def __ge__(self, other: Any) -> Any:
        return self._get_max_avg_salary() >= other._get_max_avg_salary()

    def __ne__(self, other: Any) -> Any:
        return self._get_max_avg_salary() != other._get_max_avg_salary()


if __name__ == "__main__":
    # data = GetVacancies("python")
    # sorted_vacancies = OperationsWithVacancies("python", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    # print(sorted_vacancies._filtered_vacancies())
    # sorted_vacancies_2 = OperationsWithVacancies("java", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    # print(sorted_vacancies_2.avg())
    salary_vacancies = SalaryOfVacancies("python", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    # salary_vacancies_2 = SalaryOfVacancies("java", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    print(salary_vacancies._comparison_pay())
    # if salary_vacancies > salary_vacancies_2:
    #     print("Python vacancies have a higher average salary.")
    # elif salary_vacancies < salary_vacancies_2:
    #     print("Java vacancies have a higher average salary.")
    # else:
    #     print("Both have the same average salary.")
    #
    # if salary_vacancies != salary_vacancies_2:
    #     print("Не равно.")
    # else:
    #     print("Равно.")
