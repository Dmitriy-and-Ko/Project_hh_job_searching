import json
from typing import List
from vacancy import Vacancy


class VacancyFileManager:
    @staticmethod
    def save_to_file(vacancies: List[Vacancy], filename: str):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump([v.__dict__ for v in vacancies], file, ensure_ascii=False, indent=4)

    @staticmethod
    def load_from_file(filename: str) -> List[Vacancy]:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [Vacancy(**item) for item in data]
