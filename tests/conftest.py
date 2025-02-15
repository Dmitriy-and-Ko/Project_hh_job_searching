import pytest
from src.api_hh import HHJobPlatform
from src.vacancy import Vacancy
from src.abstract import JobPlatformAPI


@pytest.fixture()
def head_hunter_example():
    return HHJobPlatform(
        base_url="https://api.hh.ru/vacancies"
    )


@pytest.fixture()
def vacancy_Python_developer():
    return Vacancy(
        name="Python_developer",
        url="https://hh.ru/applicant/vacancy_response?vacancyId=117286365",
        salary_from=100000,
        salary_to=120000,
        description="Разработка и поддержка, back end части веб-приложений."
    )