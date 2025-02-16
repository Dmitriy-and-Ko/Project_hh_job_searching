import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, List

from src.vacancy import Vacancy

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
            with open(self.file_path, "r", encoding="utf-8") as file:
                content = file.read().strip()
                return json.loads(content) if content else []  # Загружаем только если не пусто
        except FileNotFoundError:
            return []

    def _save_data(self, data):
        with open(self.file_path, "w", encoding="utf-8") as file:
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
