import pytest
from src.vacancy import Vacancy  # Импортируем класс Vacancy
from src.abstract import JobPlatformAPI

# Тестирование создания объекта Vacancy
def test_vacancy_init(vacancy_Python_developer):

    assert vacancy_Python_developer.name == "Python_developer"
    assert vacancy_Python_developer.url == "https://hh.ru/applicant/vacancy_response?vacancyId=117286365"
    assert vacancy_Python_developer.salary_from == 100000
    assert vacancy_Python_developer.salary_to == 120000
    assert vacancy_Python_developer.description == "Разработка и поддержка, back end части веб-приложений."


# Тестирование того, что при отсутствии зарплаты по умолчанию устанавливается 0
# def test_create_vacancy_with_default_salary():
#     vacancy = Vacancy(name="Программист Python", url="https://example.com")
#
#     assert vacancy.salary_from == 0
#     assert vacancy.salary_to == 0
#
#
# # Тестирование того, что выбрасывается ошибка при отсутствии обязательных данных
# def test_create_vacancy_without_name():
#     with pytest.raises(ValueError, match="Название вакансии и URL обязательны."):
#         Vacancy(name="", url="https://example.com")
#
#
# # Тестирование метода __lt__ (меньше)
# def test_vacancy_comparison_lt():
#     vacancy1 = Vacancy(name="Вакансия 1", url="https://example1.com", salary_from=100000, salary_to=150000)
#     vacancy2 = Vacancy(name="Вакансия 2", url="https://example2.com", salary_from=120000, salary_to=160000)
#
#     assert vacancy1 < vacancy2
#
#
# # Тестирование метода __gt__ (больше)
# def test_vacancy_comparison_gt():
#     vacancy1 = Vacancy(name="Вакансия 1", url="https://example1.com", salary_from=100000, salary_to=150000)
#     vacancy2 = Vacancy(name="Вакансия 2", url="https://example2.com", salary_from=120000, salary_to=160000)
#
#     assert vacancy2 > vacancy1
#
#
# # Тестирование метода validate (с отрицательной зарплатой)
# def test_validate_invalid_salary():
#     with pytest.raises(ValueError, match="Зарплата не может быть меньше 0."):
#         vacancy = Vacancy(name="Программист Python", url="https://example.com", salary_from=-100000)

