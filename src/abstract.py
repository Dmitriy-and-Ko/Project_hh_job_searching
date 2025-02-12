from abc import ABC, abstractmethod

class VacancyAPI(ABC):
    @abstractmethod
    def fetch_vacancies(self, query: str, area: str = "1"):
        """Получить вакансии по запросу"""
        pass
