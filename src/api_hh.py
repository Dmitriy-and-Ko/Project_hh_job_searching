import requests
from abstract import JobPlatformAPI

"""Kласс, который будет наследовать JobPlatformAPI и реализовывать методы для получения данных с 
платформы hh.ru."""


class HHJobPlatform(JobPlatformAPI):
    def __init__(self, base_url="https://api.hh.ru/vacancies"):
        self.base_url = base_url

    def connect(self):
        # Просто проверим доступность API
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Ошибка подключения: {e}")
            return False

    def get_vacancies(self, search_query: str, page: int = 1, area: int =1):
        """Получаем вакансии с платформы hh.ru"""
        params = {'text': search_query, 'page': page, 'area': area}
        # params = {'text': search_query, 'page': page, 'per_page': per_page, 'area': area}
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()['items']
        else:
            print(f"Ошибка получения данных: {response.status_code}")
            return []


if __name__ == "__main__":
    url_ex = HHJobPlatform()
    hh_url = url_ex.base_url
    print(hh_url)

    response = url_ex.get_vacancies("Электрик", 12, 3)
    print(response)
    # status = response.status_code
    # result = response.text
    # print(status)
    # print(result)
    #
    # class_url = HhApi()
    #
    # response_2 = class_url.fetch_vacancies()
