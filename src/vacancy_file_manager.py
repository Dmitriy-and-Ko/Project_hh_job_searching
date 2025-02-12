import json
from typing import List
from vacancy import Vacancy


import json
from abc import ABC, abstractmethod

"""Абстрактный класс для работы с файлами, который позволит сохранять вакансии, читать их и удалять. 
Реализуем его для работы с JSON."""


class JobFileStorage(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        """Добавить вакансию в файл"""
        pass

    @abstractmethod
    def get_vacancies(self, search_query: str):
        """Получить вакансии по запросу"""
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy_url: str):
        """Удалить вакансию по URL"""
        pass


class JSONJobFileStorage(JobFileStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def _load_data(self):
        """Загрузить данные из файла"""
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def _save_data(self, data):
        """Сохранить данные в файл"""
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy: Vacancy):
        data = self._load_data()
        data.append(vacancy.__dict__)
        self._save_data(data)

    def get_vacancies(self, search_query: str):
        data = self._load_data()
        return [Vacancy(**vacancy) for vacancy in data if search_query.lower() in vacancy["name"].lower()]

    def remove_vacancy(self, vacancy_url: str):
        data = self._load_data()
        data = [vacancy for vacancy in data if vacancy["url"] != vacancy_url]
        self._save_data(data)
