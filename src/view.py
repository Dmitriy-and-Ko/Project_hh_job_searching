from src.api_hh import HHJobPlatform
from src.vacancy import Vacancy
from src.vacancy_file_manager import JSONVacancyStorage

"""Функция для взаимодействия с пользователем через консоль, которая будет запрашивать данные,
 отображать результаты и позволять фильтровать вакансии."""


def user_interaction():
    platform = HHJobPlatform()
    storage = JSONVacancyStorage("C:/Users/user/OneDrive/Desktop/my-prj/Project_job_seerch/data/hh_vacancies.json")

    if not platform.connect():
        print("Не удалось подключиться к API hh.ru")
        return

    while True:
        print("\n1. Ввести поисковый запрос")
        print("2. Получить топ N вакансий по зарплате")
        print("3. Найти вакансии по ключевому слову в описании")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            query = input("Введите поисковый запрос: ")
            vacancies = platform.get_vacancies(query)
            vacancies_list = Vacancy.from_platform(vacancies)
            storage.add_vacancies(vacancies_list)
            print(f"Добавлено {len(vacancies_list)} вакансий.")

        elif choice == "2":
            n = int(input("Сколько вакансий вывести?: "))
            data = storage._load_data()
            vacancies_list = [Vacancy(**vacancy) for vacancy in data]  # Преобразуем словари в объекты Vacancy
            sorted_vacancies = sorted(vacancies_list, key=lambda x: (x.salary_from + x.salary_to) / 2, reverse=True)
            for vacancy in sorted_vacancies[:n]:
                print(vacancy.__str__())

        elif choice == "3":
            keyword = input("Введите ключевое слово: ")
            data = storage._load_data()
            filtered = [v for v in data if keyword.lower() in v["description"].lower()]
            for vacancy in filtered:
                print(vacancy)

        elif choice == "4":
            break

        else:
            print("Неверный выбор, попробуйте снова.")
