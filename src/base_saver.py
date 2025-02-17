from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class BaseVacanciesSaver(ABC):
    """
    Абстрактный класс для добавления вакансий в файл,
    получения данных из файла по указанным критериям
    и удаления информации о вакансиях
    """

    @abstractmethod
    def _read_vacancies(self) -> None:
        """Метод для загрузки данных из файла"""
        pass

    @abstractmethod
    def _write_vacancies(self, vacancies: list[Vacancy]) -> None:
        """Метод для записи данных в файл"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Метод для удаления данных из файла"""
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Метод для сохранения данных в файл."""
        pass
