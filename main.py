from src.head_hunter_api import HeadHunterAPI
from src.vacancy import Vacancy
from src.vacancy_manager import VacancyManager


def user_interaction() -> None:
    """Функция для взаимодействия с пользователем"""
    while True:
        search_query = input("Введите поисковый запрос: ")
        if search_query:
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")
    while True:
        top_n = input("Введите количество вакансий для вывода в топ N (число): ")
        if top_n.isdigit():
            top_n = int(top_n)
            break
        else:
            print("Некорректный ввод. Введите число для количества вакансий.")

    while True:
        filter_experience = input("Введите Ваш опыт (число): ")
        if filter_experience.isdigit():
            filter_experience = int(filter_experience)
            break
        else:
            print("Некорректный ввод. Введите число для опыта работы.")

    while True:
        salary_range = input("Введите диапазон зарплат числами через тире: ")  # Пример: 100000 - 150000
        try:
            min_input_salary, max_input_salary = map(int, salary_range.split("-"))
            break
        except ValueError:
            print("Неверный формат зарплаты. Используйте формат: 'минимум-maximum' (например, 100000-150000)")

    while True:
        sort_vacancies = input(
            "Если хотите отсортировать вакансии 'по возрастанию' введите 1; если 'по убыванию' введите 2): "
        )
        if sort_vacancies in ["1", "2"]:
            break
        else:
            print("Некорректный ввод. Введите 1 для возрастания или 2 для убывания.")

    add_delete_exit_choice = input(
        "Если хотите добавить в файл определенную вакансию введите '1';\n"
        "Если хотите удалить из файла определенную вакансию введите '2';\n"
        "Любой другой ввод будет означать выход: "
    )

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.load_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    vacancy_manager = VacancyManager()
    vacancy_manager.vacancies_list = vacancies_list
    vacancy_manager.filter_vacancies(filter_experience)
    vacancy_manager.sort_vacancies(sort_vacancies)
    vacancy_manager.get_vacancies_by_salary(min_input_salary, max_input_salary)
    vacancy_manager.get_top_vacancies(top_n)

    vacancies_str = vacancy_manager.print_vacancies()
    print("Вакансии по вашему запросу:")
    print("\n".join(vacancies_str))

    vacancy_manager.add_or_delete_choice(add_delete_exit_choice)
    print("Программа завершила свою работу!")


# Пример работы функции
if __name__ == "__main__":
    user_interaction()
