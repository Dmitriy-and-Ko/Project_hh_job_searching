from vacancy import Vacancy
from vacancy_file_manager import VacancyFileManager
from src.api_hh import HhApi


def user_interface():
    print("Программа для поиска вакансий с hh.ru")
    api = HhApi()
    vacancies = []

    while True:
        print("\nМеню:")
        print("1. Поиск вакансий по запросу")
        print("2. Получить топ N вакансий по зарплате")
        print("3. Получить вакансии с ключевым словом в описании")
        print("4. Выход")

        choice = input("Выберите опцию: ")

        if choice == '1':
            query = input("Введите поисковый запрос: ")
            vacancies_data = api.fetch_vacancies(query)
            vacancies = [Vacancy(v['name'], v['alternate_url'], v['salary']['from'] if v['salary'] else None,
                                 v['snippet']['requirement']) for v in vacancies_data]
            print(f"Найдено {len(vacancies)} вакансий.")

        elif choice == '2':
            n = int(input("Введите количество вакансий для отображения: "))
            top_vacancies = sorted(vacancies, reverse=True)[:n]
            for vac in top_vacancies:
                print(f"{vac.title} - {vac.salary}")

        elif choice == '3':
            keyword = input("Введите ключевое слово: ")
            filtered_vacancies = [vac for vac in vacancies if keyword.lower() in vac.description.lower()]
            for vac in filtered_vacancies:
                print(f"{vac.title} - {vac.salary}")

        elif choice == '4':
            filename = input("Введите имя файла для сохранения вакансий (например, vacancies.json): ")
            VacancyFileManager.save_to_file(vacancies, filename)
            print(f"Вакансии сохранены в {filename}.")
            break
