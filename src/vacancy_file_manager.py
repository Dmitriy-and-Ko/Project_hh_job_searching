
from src.vacancy import Vacancy
from typing import List, Dict
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
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            self._save_data([])  # Создаём пустой JSON, если файла нет

    def _load_data(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                content = file.read().strip()
                return json.loads(content) if content else []  # Загружаем только если не пусто
        except FileNotFoundError:
            return []

    def _save_data(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_vacancies(self, vacancies: List[Vacancy]):
        data = self._load_data()
        for vacancy in vacancies:
            data.append(vacancy.to_dict())  # Используем метод to_dict() у класса Vacancy
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
    storage = JSONVacancyStorage("C:/Users/user/OneDrive/Desktop/my-prj/Project_job_seerch/data/hh_vacancies.json")
    print(storage.file_path)

    # Очистим файл перед тестом
    storage._save_data([])

    # Добавляем несколько вакансий
    vacancy1 = Vacancy("Python Developer", "https://example.com/1", 100000, 120000, "Разработка приложений")
    vacancy2 = Vacancy("Data Scientist", "https://example.com/2", 150000, 200000, "Анализ данных")
    vacancy3 = Vacancy("Python Developer", "https://example.com/3", 130000, 150000, "Работа с данными")

    storage.add_vacancies([vacancy1, vacancy2, vacancy3])
    print("Вакансии добавлены.")

    # Проверяем get_vacancies без критериев
    print("\nВсе вакансии:")
    print(storage.get_vacancies({}))

    # Фильтр по названию
    print("\nВакансии с названием 'Python Developer':")
    print(storage.get_vacancies({"title": "Python Developer"}))

    # Фильтр по зарплате
    print("\nВакансии с зарплатой от 150000:")
    print(storage.get_vacancies({"salary_from": 150000}))

    # Фильтр по URL
    print("\nВакансия с URL 'https://example.com/2':")
    print(storage.get_vacancies({"url": "https://example.com/2"}))

    # Удаляем вакансию 'Python Developer'
    storage.delete_vacancies({"title": "Python Developer"})
    print("\nПосле удаления вакансии 'Python Developer':")
    print(storage.get_vacancies({}))

    # Удаляем вакансию 'Data Scientist'
    storage.delete_vacancies({"title": "Data Scientist"})
    print("\nПосле удаления вакансии 'Data Scientist':")
    print(storage.get_vacancies({}))

    # Пытаемся удалить несуществующую вакансию
    storage.delete_vacancies({"title": "Frontend Developer"})
    print("\nПосле попытки удаления несуществующей вакансии 'Frontend Developer':")
    print(storage.get_vacancies({}))

