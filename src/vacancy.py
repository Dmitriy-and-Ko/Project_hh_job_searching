import re


class Vacancy:
    def __init__(self, title, url, salary, description):
        self.title = title
        self.url = url
        self.salary = salary
        self.description = description

        # Валидация данных
        self.validate()

    def validate(self):
        """Проверка валидности данных вакансии"""
        if not self.salary:
            self.salary = "Зарплата не указана"
        if not isinstance(self.salary, (int, float)):
            self.salary = 0

    def __lt__(self, other):
        """Сравнение вакансий по зарплате"""
        return self.salary < other.salary

    def __repr__(self):
        return f"Vacancy(title={self.title}, salary={self.salary})"
