from src.api_hh import HHJobPlatform
import pytest
from src.abstract import JobPlatformAPI
from unittest.mock import patch

def test_hh_api_init(head_hunter_example):
    assert head_hunter_example.base_url == "https://api.hh.ru/vacancies"


def test_connect_success(mock_hh_api):
    """Тест на успешное подключение к API."""
    with patch('requests.get') as mock_get:
        # Мокаем успешный ответ от API
        mock_get.return_value.status_code = 200

        assert mock_hh_api.connect() is True


# def test_connect_failure(mock_hh_api):
#     """Тест на ошибку подключения к API."""
#     with patch('requests.get') as mock_get:
#         # Мокаем неудачный ответ от API
#         mock_get.return_value.status_code = 500
#
#         assert mock_hh_api.connect() is False


def test_get_vacancies_success(mock_hh_api):
    """Тест на успешное получение вакансий."""
    with patch('requests.get') as mock_get:
        # Мокаем успешный ответ от API с вакансией
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'items': [{'id': 1, 'name': 'Developer'}]}

        vacancies = mock_hh_api.get_vacancies('developer')
        assert len(vacancies) == 1
        assert vacancies[0]['name'] == 'Developer'


def test_get_vacancies_failure(mock_hh_api):
    """Тест на неудачное получение вакансий."""
    with patch('requests.get') as mock_get:
        # Мокаем неудачный ответ от API
        mock_get.return_value.status_code = 500

        vacancies = mock_hh_api.get_vacancies('developer')
        assert vacancies == []


# def test_get_all_vacancies_pagination(mock_hh_api):
#     """Тест на получение всех вакансий с учетом пагинации."""
#     with patch('requests.get') as mock_get:
#         # Мокаем первый ответ с несколькими страницами
#         mock_get.return_value.status_code = 200
#         mock_get.return_value.json.side_effect = [
#             {'items': [{'id': 1, 'name': 'Developer 1'}], 'pages': 2},  # Страница 1
#             {'items': [{'id': 2, 'name': 'Developer 2'}], 'pages': 2},  # Страница 2
#         ]
#
#         all_vacancies = mock_hh_api.get_all_vacancies('developer')
#
#         assert len(all_vacancies) == 2
#         assert all_vacancies[0]['name'] == 'Developer 1'
#         assert all_vacancies[1]['name'] == 'Developer 2'

# def test_get_vacancies_invalid_json(mock_hh_api):
#     """Тест на ошибку парсинга JSON."""
#     with patch('requests.get') as mock_get:
#         # Мокаем ответ с неправильным JSON
#         mock_get.return_value.status_code = 200
#         mock_get.return_value.json.side_effect = ValueError("Invalid JSON")
#
#         vacancies = mock_hh_api.get_vacancies('developer')
#         assert vacancies == []