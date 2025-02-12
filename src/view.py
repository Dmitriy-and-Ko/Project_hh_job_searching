from vacancy import Vacancy
from vacancy_file_manager import JSONJobFileStorage
from src.api_hh import HHJobPlatform

"""Функция для взаимодействия с пользователем через консоль, которая будет запрашивать данные,
 отображать результаты и позволять фильтровать вакансии."""


def user_interaction():
    hh_platform = HHJobPlatform()
    if not hh_platform.connect():
        return

    storage = JSONJobFileStorage('vacancies.json')

    while True:
        print("\nМеню:")
        print("1. Поиск вакансий")
        print("2. Топ N вакансий по зарплате")
        print("3. Вакансии с ключевым словом в описании")
        print("4. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            search_query = input("Введите поисковый запрос: ")
            vacancies = hh_platform.get_vacancies(search_query)
            for vacancy in vacancies:
                v = Vacancy(vacancy["name"], vacancy["url"], vacancy["salary_from"], vacancy["salary_to"],
                            vacancy["description"])
                storage.add_vacancy(v)
            print(f"Найдено {len(vacancies)} вакансий.")

        elif choice == "2":
            N = int(input("Введите количество вакансий для отображения: "))
            vacancies = storage.get_vacancies("")
            vacancies.sort(reverse=True)
            for v in vacancies[:N]:
                print(v)

        elif choice == "3":
            keyword = input("Введите ключевое слово для поиска в описаниях: ")
            vacancies = storage.get_vacancies(keyword)
            for v in vacancies:
                print(v)

        elif choice == "4":
            break

