from src.GetVacancies import GetVacancies


class OperationsWithVacancies(GetVacancies):
    """Класс для работы с вакансиями"""

    try:
        __slots__ = ("keyword", "keyword_2", "employment", "currency", "pay_from", "pay_to")

        def __init__(self, keyword, keyword_2, employment, currency, pay_from, pay_to):
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
            self.sorted_vacancies = []

        def _filtered_vacancies(self):
            """Метод, фильтрует вакансии по фильтрам"""
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

        def _avg(self):
            """Метод, высчитывающий среднюю зарплату для каждой вакансии"""
            self._filtered_vacancies()
            for vacancy in self.sorted_vacancies:
                avg_pay = (vacancy["salary"].get("from") + vacancy["salary"].get("to")) / 2
                vacancy["salary"]["avg"] = avg_pay
            return self.sorted_vacancies

        def _comparison_pay(self):
            """Метод, сортирующий вакансии со средними зарплатами в порядке возрастания"""
            self._avg()
            if not self.sorted_vacancies:
                return None
            return sorted(self.sorted_vacancies, key=lambda x: x["salary"]["avg"], reverse=True)

        def _highest_pay(self):
            """Метод, возвращающий вакансию с максимальной средней зарплатой"""
            self._avg()
            if not self.sorted_vacancies:
                return None
            return max(self.sorted_vacancies, key=lambda x: x["salary"]["avg"])

        def _lowest_pay(self):
            """Метод, возвращающий вакансию с минимальной средней зарплатой"""
            self._avg()
            if not self.sorted_vacancies:
                return None
            return min(self.sorted_vacancies, key=lambda x: x["salary"]["avg"])

        def _get_max_avg_salary(self):
            """Метод возвращает максимальную среднюю зарплату в списке вакансий"""
            self._avg()
            highest_vacancy = self._highest_pay()
            return highest_vacancy["salary"]["avg"] if highest_vacancy else 0

        def __eq__(self, other):
            return self._get_max_avg_salary() == other._get_max_avg_salary()

        def __lt__(self, other):
            return self._get_max_avg_salary() < other._get_max_avg_salary()

        def __le__(self, other):
            return self._get_max_avg_salary() <= other._get_max_avg_salary()

        def __gt__(self, other):
            return self._get_max_avg_salary() > other._get_max_avg_salary()

        def __ge__(self, other):
            return self._get_max_avg_salary() >= other._get_max_avg_salary()

        def __ne__(self, other):
            return self._get_max_avg_salary() != other._get_max_avg_salary()

    except Exception as e:
        print(e)
        print("Ошибка в классе OperationsWithVacancies")


if __name__ == "__main__":
    data = GetVacancies("python")
    sorted_vacancies = OperationsWithVacancies("python", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    # print(sorted_vacancies.avg())
    sorted_vacancies_2 = OperationsWithVacancies("java", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    # print(sorted_vacancies_2.avg())

    if sorted_vacancies > sorted_vacancies_2:
        print("Python vacancies have a higher average salary.")
    elif sorted_vacancies < sorted_vacancies_2:
        print("Java vacancies have a higher average salary.")
    else:
        print("Both have the same average salary.")
