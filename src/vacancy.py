import re

"""Класс, который будет представлять вакансию с атрибутами, такими как название, ссылка, зарплата, описание, 
а также методы для сравнения вакансий по зарплате и валидации данных."""

class Vacancy:
    def __init__(self, name, url, salary_from=None, salary_to=None, description=None):
        self.name = name
        self.url = url
        self.salary_from = salary_from if salary_from is not None else 0
        self.salary_to = salary_to if salary_to is not None else 0
        self.description = description or "Описание не указано"

        # Валидация данных
        self.validate()

    def validate(self):
        """Метод для валидации данных вакансии"""
        if not self.name or not self.url:
            raise ValueError("Название вакансии и URL обязательны.")
        if self.salary_from < 0 or self.salary_to < 0:
            raise ValueError("Зарплата не может быть меньше 0.")

    def __str__(self):
        return f"Вакансия: {self.name}, Зарплата: {self.salary_from}-{self.salary_to}, URL: {self.url}"

    def __lt__(self, other):
        """Сравнение вакансий по минимальной зарплате"""
        return (self.salary_from + self.salary_to) / 2 < (other.salary_from + other.salary_to) / 2

    def __gt__(self, other):
        """Сравнение вакансий по максимальной зарплате"""
        return (self.salary_from + self.salary_to) / 2 > (other.salary_from + other.salary_to) / 2
