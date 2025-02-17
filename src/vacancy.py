from typing import List, Optional


class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ["name", "url", "city", "salary", "experience"]

    def __init__(
        self, name: str, url: str, city: str, salary: Optional[int] = None, experience: Optional[str] = None
    ) -> None:
        self.name: str = name
        self.url: str = url
        self.city: str = city
        self.salary: int = self._validate_salary(salary)  # Валидация зарплаты
        self.experience: str = self._validate_experience(experience)  # Валидация опыта

    def __eq__(self, other: object) -> bool:
        """Сравнение вакансий по всем атрибутам"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return (
            self.name == other.name
            and self.url == other.url
            and self.city == other.city
            and self.salary == other.salary
            and self.experience == other.experience
        )

    def __lt__(self, other: "Vacancy") -> bool:
        """Сравнение вакансий по зарплате (меньше)"""
        if not isinstance(other, Vacancy):
            return False
        return (
            self.salary < other.salary
            if isinstance(self.salary, (int, float)) and isinstance(other.salary, (int, float))
            else False
        )

    def __gt__(self, other: "Vacancy") -> bool:
        """Сравнение вакансий по зарплате (больше)"""
        if not isinstance(other, Vacancy):
            return False
        return (
            self.salary > other.salary
            if isinstance(self.salary, (int, float)) and isinstance(other.salary, (int, float))
            else False
        )

    def __str__(self) -> str:
        """Строковое представление для экземпляра класса вакансия"""
        return f"Вакансия: '{self.name}', Ссылка на вакансию: '{self.url}', Город: '{self.city}', \
Заработная плата: {self.salary}, Опыт: '{self.experience}')"

    @classmethod
    def cast_to_object_list(cls, data: list[dict]) -> list["Vacancy"]:
        """Метод для преобразования списка вакансий в список объектов Vacancy"""
        vacancy_list: List["Vacancy"] = []
        for opening in data:
            vacancy = cls(
                name=opening.get("name", ""),
                url=opening.get("url", ""),
                city=opening.get("city", ""),
                salary=opening.get("salary", None),
                experience=opening.get("experience", None),
            )
            vacancy_list.append(vacancy)
        return vacancy_list

    @staticmethod
    def _validate_salary(salary: Optional[int]) -> int:
        """Приватный метод для валидации зарплаты"""
        if salary is None:
            return 0  # Если зарплата не указана, возвращаем 0
        elif isinstance(salary, (int, float)):
            return salary  # Если указана валидная зарплата, возвращаем её
        else:
            raise ValueError("Зарплата не валидна")  # Если тип не соответствует, вызываем исключение

    @staticmethod
    def _validate_experience(experience: Optional[str]) -> str:
        """Приватный метод для валидации опыта работы"""
        if experience is None:
            return "Не указано"  # Если опыт не указан, возвращаем дефолтное значение
        elif isinstance(experience, str) and experience.strip():
            return experience  # Если опыт указан как строка и не пустой
        else:
            raise ValueError("Опыт работы должен быть строкой и не может быть пустым.")  # Проверка на пустое значение

    @staticmethod
    def vacancy_in_dict(opening: object) -> dict:
        """Метод для преобразования объекта в тип 'словарь'"""
        try:
            if isinstance(opening, Vacancy):
                opening_dict = {
                    "name": opening.name,
                    "url": opening.url,
                    "city": opening.city,
                    "salary": opening.salary,
                    "experience": opening.experience,
                }
                return opening_dict
            else:
                raise TypeError("Объект должен быть экземпляром класса Vacancy")
        except AttributeError as e:
            raise ValueError(f"Ошибка при доступе к атрибуту: {e}")
