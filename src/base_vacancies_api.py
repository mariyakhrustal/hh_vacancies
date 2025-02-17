from abc import ABC, abstractmethod


class BaseVacanciesAPI(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def _connect_to_api(self, params: dict) -> None:
        """Метод для подключения к API сервису"""
        pass

    @abstractmethod
    def load_vacancies(self, keyword: str) -> None:
        """Метод для получения вакансий по запросу"""
        pass
