import requests
from abstract import VacancyAPI


class HhApi(VacancyAPI):
    def __init__(self):
        self.base_url = "https://api.hh.ru/vacancies"

    def fetch_vacancies(self, query: str, area: str = "1"):
        params = {"text": query, "area": area}
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()['items']
        else:
            return []

if __name__ == "__main__":
    url = HhApi().base_url
    response = requests.get(url)
    status = response.status_code
    result = response.text
    print(status)
    print(result)
