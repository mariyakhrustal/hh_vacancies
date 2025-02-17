from typing import Any

import requests

from src.base_vacancies_api import BaseVacanciesAPI


class HeadHunterAPI(BaseVacanciesAPI):
    """Класс для работы с платформой hh.ru"""

    def __init__(self) -> None:
        self.__base_url = "https://api.hh.ru"
        self.__params = {
            "text": "Python Developer",
            "search_field": "name",
            "area": 113,
            "period": 1,
            "only_with_salary": True,
            "per_page": 100,
            "page": 0,
        }
        self.__vacancies: list = []

    def _connect_to_api(self, params: dict) -> Any:
        """Метод для подключения к API сервису"""
        try:
            url = f"{self.__base_url}/vacancies"
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Ошибка при запросе вакансий: {response.status_code}")
                return []
        except Exception as e:
            print(f"Ошибка: {e}")
            return []

    def load_vacancies(self, keyword: str) -> Any:
        """Метод для получения вакансий по запросу"""
        self.__params["text"] = keyword
        vacancies = []
        while True:
            data = self._connect_to_api(self.__params)
            if not data or "items" not in data:
                break
            vacancies.extend(data["items"])
            if data["pages"] <= self.__params["page"]:
                break
            else:
                self.__params["page"] += 1
        result = [
            {
                "name": vacancy["name"],
                "url": vacancy["alternate_url"],
                "salary": vacancy["salary"]["from"] if vacancy["salary"]["from"] is not None else 0,
                "city": vacancy["area"]["name"],
                "experience": vacancy["experience"]["name"] if vacancy["experience"]["name"] is not None else "None",
            }
            for vacancy in vacancies
        ]
        self.__vacancies.extend(result)
        return self.__vacancies
