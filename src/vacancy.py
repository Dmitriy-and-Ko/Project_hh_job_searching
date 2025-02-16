import requests
from src.api_hh import HHJobPlatform

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

    @staticmethod
    def from_platform(platform_data):
        """Метод для формирования списка вакансий из данных платформы"""
        vacancies = []
        for job_data in platform_data:
            # Извлекаем необходимые данные из вложенных словарей с проверками на None
            name = job_data.get('name', 'Название не указано')
            url = job_data.get('apply_alternate_url', '')  # Например, можно взять альтернативный URL отклика

            # Извлекаем данные по зарплате, добавляем проверку на None
            salary_from = job_data.get('salary', {}).get('from', 0) if job_data.get('salary') else 0
            salary_to = job_data.get('salary', {}).get('to', 0) if job_data.get('salary') else 0

            # Извлекаем описание из department с дополнительной проверкой на None
            department = job_data.get('department')
            description = department.get('name', 'Описание не указано') if department else 'Описание не указано'

            # Создаем объект Vacancy с полученными данными
            vacancy = Vacancy(
                name=name,
                url=url,
                salary_from=salary_from,
                salary_to=salary_to,
                description=description
            )
            vacancies.append(vacancy)
        return vacancies


if __name__ == '__main__':
    platform = HHJobPlatform()

    # Проверяем подключение
    if platform.connect():
        # Получаем вакансии с платформы по запросу
        platform_data = platform.get_vacancies("python разработчик")

        # Преобразуем данные вакансий в экземпляры класса Vacancy
        vacancies = Vacancy.from_platform(platform_data)

        # Выводим вакансии
        for vacancy in vacancies:
            print(vacancy)
        print(type(vacancy))

    # vacancy_developer = Vacancy(name="Python_developer",
    #     url="https://hh.ru/applicant/vacancy_response?vacancyId=117286365",
    #     salary_from=100000,
    #     salary_to=120000,
    #     description="Разработка и поддержка, back end части веб-приложений.")
    #
    # print(vacancy_developer.__str__())