import pytest

from src.vacancy import Vacancy


def test_vacancy_init(vacancy_1: Vacancy) -> None:
    """Тест на инициализацию объекта Vacancy"""
    assert vacancy_1.name == "Python Developer"
    assert vacancy_1.url == "https://example.com"
    assert vacancy_1.city == "Москва"
    assert vacancy_1.salary == 100000
    assert vacancy_1.experience == "2 года"


def test_create_vacancy_default_values() -> None:
    """Тест на инициализацию объекта Vacancy со значениями по умолчанию"""
    vacancy = Vacancy(name="Python Developer", url="https://example.com", city="Москва")

    assert vacancy.salary == 0
    assert vacancy.experience == "Не указано"


def test_invalid_salary() -> None:
    """Тест на валидацию зарплаты"""
    with pytest.raises(ValueError):
        Vacancy(name="Python Developer", url="https://example.com", city="Москва", salary="invalid_salary")


def test_invalid_experience() -> None:
    """Тест на валидацию опыта"""
    with pytest.raises(ValueError):
        Vacancy(name="Python Developer", url="https://example.com", city="Москва", experience="")


def test_vacancy_str_print(vacancy_1: Vacancy) -> None:
    """Тест на строковое представление для экземпляра класса вакансия"""
    assert (
        str(vacancy_1)
        == "Вакансия: 'Python Developer', Ссылка на вакансию: 'https://example.com', \
Город: 'Москва', Заработная плата: 100000, Опыт: '2 года')"
    )


def test_vacancy_equality(vacancy_1: Vacancy, vacancy_2: Vacancy) -> None:
    """Тест на сравнение вакансий по всем атрибутам"""
    vacancy = Vacancy(
        name="Python Developer", url="https://example.com", city="Москва", salary=100000, experience="2 года"
    )
    assert vacancy_1 != vacancy_2
    assert vacancy_1 == vacancy
    with pytest.raises(TypeError):
        vacancy_2 == "1"


def test_vacancy_salary_lt(vacancy_1: Vacancy, vacancy_2: Vacancy) -> None:
    """Тест на сравнение вакансий по зарплате (меньше)"""
    assert vacancy_1 > vacancy_2
    with pytest.raises(TypeError, match="Оба экземпляра должны быть объектами Vacancy"):
        vacancy_2 > [1, 2]


def test_vacancy_salary_gt(vacancy_1: Vacancy, vacancy_2: Vacancy) -> None:
    """Тест на сравнение вакансий по зарплате (больше)"""
    assert vacancy_2 < vacancy_1
    with pytest.raises(TypeError, match="Оба экземпляра должны быть объектами Vacancy"):
        vacancy_2 < "2"


def test_vacancy_obj_to_dict(vacancy_2: Vacancy) -> None:
    """Тест на преобразование объекта в словарь"""
    vacancy_dict = Vacancy.vacancy_in_dict(vacancy_2)

    assert vacancy_dict["name"] == "Java Developer"
    assert vacancy_dict["url"] == "https://example.com"
    assert vacancy_dict["city"] == "Москва"
    assert vacancy_dict["salary"] == 80000
    assert vacancy_dict["experience"] == "3 года"

    with pytest.raises(TypeError):
        Vacancy.vacancy_in_dict("vacancy_2")


def test_vacancy_cast_to_object_list(vacancy_1: Vacancy, vacancy_2: Vacancy) -> None:
    """Тест на преобразование списка вакансий в список объектов Vacancy"""
    data = [
        {
            "name": "Программист",
            "url": "http://example.com",
            "city": "Москва",
            "salary": 100000,
            "experience": "2 года",
        },
        {
            "name": "Менеджер",
            "url": "http://example.com",
            "city": "Санкт-Петербург",
            "salary": 80000,
            "experience": "3 года",
        },
    ]
    vacancies = Vacancy.cast_to_object_list(data)
    assert len(vacancies) == 2
    assert vacancies[0].name == "Программист"
    assert vacancies[1].name == "Менеджер"
