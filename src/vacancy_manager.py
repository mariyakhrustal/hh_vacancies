from typing import Any

from src.json_saver import JSONSaver


class VacancyManager:
    """Класс для управления вакансиями: поиск, фильтрация, сортировка"""

    def __init__(self) -> None:
        self.vacancies_list: list = []

    def filter_vacancies(self, experience: Any) -> list["VacancyManager"]:
        """Фильтрует вакансии по опыту работы"""
        if experience == 0:
            self.vacancies_list = [
                vacancy for vacancy in self.vacancies_list if "нет опыта" in vacancy.experience.lower()
            ]
        elif 1 <= experience <= 3:
            self.vacancies_list = [
                vacancy for vacancy in self.vacancies_list if "от 1 года до 3 лет" in vacancy.experience.lower()
            ]
        elif 3 < experience <= 6:
            self.vacancies_list = [
                vacancy for vacancy in self.vacancies_list if "от 3 до 6 лет" in vacancy.experience.lower()
            ]
        elif experience >= 6:
            self.vacancies_list = [
                vacancy for vacancy in self.vacancies_list if "более 6 лет" in vacancy.experience.lower()
            ]
        return self.vacancies_list

    def get_vacancies_by_salary(self, min_input_salary: int, max_input_salary: int) -> list["VacancyManager"]:
        """Сортирует вакансии по зарплате в заданном диапазоне"""
        self.vacancies_list = [
            vacancy for vacancy in self.vacancies_list if min_input_salary <= vacancy.salary <= max_input_salary
        ]
        return self.vacancies_list

    def sort_vacancies(self, sort_param: str) -> list["VacancyManager"]:
        """Сортировка вакансий по зарплате в зависимости от выбора пользователя"""
        if sort_param == "1":
            self.vacancies_list.sort(key=lambda vacancy: vacancy.salary)
        elif sort_param == "2":
            self.vacancies_list.sort(key=lambda vacancy: vacancy.salary, reverse=True)
        return self.vacancies_list

    def get_top_vacancies(self, top_n: Any) -> list["VacancyManager"]:
        """Возвращает топ N вакансий по зарплате"""
        top_vacancies = sorted(self.vacancies_list, key=lambda vacancy: vacancy.salary, reverse=True)
        self.vacancies_list = top_vacancies[:top_n]
        return self.vacancies_list

    def print_vacancies(self) -> list:
        """Выводит вакансии в читаемом виде"""
        if not self.vacancies_list:
            return ["Нет вакансий для отображения"]
        vacancies_str_list = [str(vacancy) for vacancy in self.vacancies_list]
        return vacancies_str_list

    def add_or_delete_choice(self, choice_number: str) -> None:
        """Метод для выбора пользователя добавить, удалить вакансию или выйти из программы"""
        if choice_number not in ["1", "2"]:
            print("Программа завершила свою работу!")
            return
        base_url = "https://hh.ru/vacancy/"
        vacancy_url = base_url + input("Допишите ссылку на вакансию для дальнейших действий: https://hh.ru/vacancy/")

        for vacancy in self.vacancies_list:
            if vacancy.url == vacancy_url:
                if choice_number == "1":
                    is_file = input(
                        "Если хотите сохранить вакансию по умолчанию ('vacancies.json'), нажмите 'Enter';\n"
                        "Если хотите сохранить в определенный файл, введите название файла: "
                    )
                    if is_file:
                        is_file += ".json"
                        json_saver = JSONSaver(is_file)
                    else:
                        json_saver = JSONSaver()
                    json_saver.add_vacancy(vacancy)
                elif choice_number == "2":
                    is_file = input(
                        "Если хотите удалить вакансию из файла по умолчанию ('vacancies.json'), нажмите 'Enter';\n"
                        "Если хотите удалить вакансию из определенного файла, введите название файла: "
                    )
                    if is_file:
                        is_file += ".json"
                        json_saver = JSONSaver(is_file)
                    else:
                        json_saver = JSONSaver()
                    json_saver.delete_vacancy(vacancy)
                return
        print("Вакансия с указанным URL не найдена.")
