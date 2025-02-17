import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancy_1():
    return Vacancy(
        name="Python Developer", url="https://example.com", city="Москва", salary=100000, experience="2 года"
    )

@pytest.fixture
def vacancy_2():
    return Vacancy(name="Java Developer", url="https://example.com", city="Москва", salary=80000, experience="3 года")

