import json

import pytest

from src.vacancy import Vacancy
from src.vacancy_file_manager import JSONVacancyStorage


def test_add_vacancies(temp_json_file, vacancy_Python_developer, vacancy_system_administrator):
    storage = JSONVacancyStorage(temp_json_file)
    storage.add_vacancies([vacancy_Python_developer, vacancy_system_administrator])

    with open(temp_json_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert len(data) == 2
    assert data[0]["name"] == vacancy_Python_developer.name
    assert data[1]["name"] == vacancy_system_administrator.name


def test_get_vacancies(temp_json_file, vacancy_Python_developer, vacancy_system_administrator):
    storage = JSONVacancyStorage(temp_json_file)
    storage.add_vacancies([vacancy_Python_developer, vacancy_system_administrator])

    result = storage.get_vacancies({"name": "Python_developer"})
    assert len(result) == 1
    assert result[0]["name"] == "Python_developer"


def test_delete_vacancies(temp_json_file, vacancy_Python_developer, vacancy_system_administrator):
    storage = JSONVacancyStorage(temp_json_file)
    storage.add_vacancies([vacancy_Python_developer, vacancy_system_administrator])

    storage.delete_vacancies({"name": "Python_developer"})
    data = storage._load_data()

    assert len(data) == 1
    assert data[0]["name"] == "Системный администратор"


def test_add_invalid_vacancy(temp_json_file, vacancy_with_negative_salary):
    storage = JSONVacancyStorage(temp_json_file)
    with pytest.raises(ValueError):
        storage.add_vacancies([Vacancy(**vacancy_with_negative_salary)])
