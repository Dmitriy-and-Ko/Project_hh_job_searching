import json
from typing import List
from src.vacancy import Vacancy
from typing import List, Dict
from src.view import PATH_TO_FILE
from pathlib import Path
import json
from abc import ABC, abstractmethod

"""Абстрактный класс для работы с файлами, который позволит сохранять вакансии, читать их и удалять. 
Реализуем его для работы с JSON."""


class VacancyStorage(ABC):
    @abstractmethod
    def add_vacancies(self, vacancies: List[Vacancy]):
        pass

    @abstractmethod
    def get_vacancies(self, criteria: Dict):
        pass

    @abstractmethod
    def delete_vacancies(self, criteria: Dict):
        pass


class JSONVacancyStorage(VacancyStorage):
    def __init__(self, file_path=PATH_TO_FILE):
        self.file_path = file_path

    def _load_data(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save_data(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_vacancies(self, vacancies: List[Vacancy]):
        data = self._load_data()
        for vacancy in vacancies:
            data.append(vacancy.__dict__)
        self._save_data(data)

    def get_vacancies(self, criteria: Dict):
        data = self._load_data()
        result = []
        for item in data:
            if all(item.get(key) == value for key, value in criteria.items()):
                result.append(item)
        return result

    def delete_vacancies(self, criteria: Dict):
        data = self._load_data()
        data = [item for item in data if not all(item.get(key) == value for key, value in criteria.items())]
        self._save_data(data)


if __name__ == "__main__":
    storage = JSONVacancyStorage("vacancies.json")

    vacancy1 = Vacancy("Python Developer", "https://example.com/1", 100000, 120000, "Разработка приложений")
    vacancy2 = Vacancy("Data Scientist", "https://example.com/2", 150000, 200000, "Анализ данных")

    # Добавляем вакансии
    storage.add_vacancies([vacancy1, vacancy2])
    print("Вакансии добавлены")

    # Получаем все вакансии
    print("Все вакансии:")
    print(storage.get_vacancies({}))

    # Фильтруем вакансии по названию
    print("Вакансии с названием Python Developer:")
    print(storage.get_vacancies({"name": "Python Developer"}))

    # Удаляем вакансию
    storage.delete_vacancies({"name": "Python Developer"})
    print("После удаления вакансии Python Developer:")
    print(storage.get_vacancies({}))

    # Удаляем тестовый файл
    import os

    os.remove("vacancies_test.json")
