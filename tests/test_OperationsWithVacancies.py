from typing import List

from src.OperationsWithVacancies import OperationsWithVacancies, SalaryOfVacancies


def test_operations_with_vacancies(input_test_operations_with_vacancies: List):
    sorted_vacancies = OperationsWithVacancies("python", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    assert sorted_vacancies._keyword == "python"
    assert sorted_vacancies.keyword_2 == "Junior"
    assert sorted_vacancies.employment == "Полная занятость"
    assert sorted_vacancies.currency == "RUR"
    assert sorted_vacancies.pay_from == 50_000
    assert sorted_vacancies.pay_to == 100_000
    assert sorted_vacancies.sorted_vacancies == []

    assert sorted_vacancies._filtered_vacancies() == input_test_operations_with_vacancies


def test_salary_of_vacancies_avg(return_test_avg):
    salary_vacancies = SalaryOfVacancies("python", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    assert salary_vacancies._avg() == return_test_avg


def test_salary_of_vacancies_comparison(return_test_comparison):
    salary_vacancies = SalaryOfVacancies("python", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    assert salary_vacancies._comparison_pay() == return_test_comparison


def test_salary_of_vacancies_highest_pay(return_test_high):
    salary_vacancies = SalaryOfVacancies("python", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    assert salary_vacancies._highest_pay() == return_test_high


def test_salary_of_vacancies_lowest_pay(return_test_lowest_pay):
    salary_vacancies = SalaryOfVacancies("python", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    assert salary_vacancies._highest_pay() == return_test_lowest_pay


def test_salary_of_vacancies_get_max_avg_salary(return_test_get_max_avg_salary):
    salary_vacancies = SalaryOfVacancies("python", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    assert salary_vacancies._get_max_avg_salary() == return_test_get_max_avg_salary


def test_salary_of_vacancies_more_or_less(return_test_get_max_avg_salary, capsys):
    salary_vacancies = SalaryOfVacancies("python", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    salary_vacancies_2 = SalaryOfVacancies("java", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    if salary_vacancies > salary_vacancies_2:
        print("Python vacancies have a higher average salary.")
    elif salary_vacancies < salary_vacancies_2:
        print("Java vacancies have a higher average salary.")
    else:
        print("Both have the same average salary.")
    message = capsys.readouterr()
    assert message.out.strip() == "Java vacancies have a higher average salary."

    if salary_vacancies != salary_vacancies_2:
        print("Не равно.")
    else:
        print("Равно.")
    message = capsys.readouterr()
    assert message.out.strip() == "Не равно."
