import json
import os
from typing import Any

from src.base_saver import BaseVacanciesSaver
from src.vacancy import Vacancy


class JSONSaver(BaseVacanciesSaver):
    """Класс для сохранения информации о вакансиях в JSON-файл"""

    def __init__(self, file_name: str = "vacancies.json") -> None:
        self._file_name = os.path.join("data", file_name)
        os.makedirs("data", exist_ok=True)

    def _read_vacancies(self) -> Any:
        """Метод для загрузки данных из файла"""
        try:
            with open(self._file_name, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _write_vacancies(self, vacancies: list[Vacancy]) -> None:
        """Метод для записи данных в файл"""
        try:
            with open(self._file_name, "w", encoding="utf-8") as f:
                json.dump(vacancies, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка при записи в файл: {e}")

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Метод для удаления данных из файла"""
        vacancies = self._read_vacancies()
        if not vacancies:
            print("Файл пуст, вакансии не найдены")
            return
        vacancy_data = vacancy.vacancy_in_dict(vacancy)
        if vacancy_data in vacancies:
            vacancies.remove(vacancy_data)
            print("Вакансия удалена")
        else:
            print("Вакансия не найдена")
        self._write_vacancies(vacancies)

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Метод для добавления данных в файл, если вакансии нет в списке"""
        vacancies = self._read_vacancies()
        try:
            vacancy_data = vacancy.vacancy_in_dict(vacancy)  # Преобразуем вакансию в словарь
            # Проверка на дублирование вакансий
            if not any(existing_vacancy == vacancy_data for existing_vacancy in vacancies):
                vacancies.append(vacancy_data)
                self._write_vacancies(vacancies)
                print(f"Вакансия добавлена в файл {self._file_name}")
            else:
                print("Вакансия уже существует в файле")
        except Exception as e:
            print(f"Ошибка при записи в файл: {e}")
