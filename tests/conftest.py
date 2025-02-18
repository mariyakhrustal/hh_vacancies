import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancy_1() -> Vacancy:
    return Vacancy(
        name="Python Developer", url="https://example.com", city="Москва", salary=100000, experience="2 года"
    )

@pytest.fixture
def vacancy_2() -> Vacancy:
    return Vacancy(name="Java Developer", url="https://example.com", city="Москва", salary=80000, experience="3 года")

@pytest.fixture
def json_response_200() -> dict:
    response = {
  "items": [
    {
      "id": "1234567",
      "name": "Python Developer",
      "alternate_url": "https://hh.ru/vacancy/1234567",
      "salary": {"from": 1000, "to": 2000, "currency": "RUB", "gross": True},
      "area": {"id": "1", "name": "Moscow"},
      "experience": {"id": "1", "name": "1-3 years"}
    },
    {
      "id": "1234568",
      "name": "Senior Python Developer",
      "alternate_url": "https://hh.ru/vacancy/1234568",
      "salary": {"from": 2000, "to": 5000, "currency": "RUB", "gross": True},
      "area": {"id": "2", "name": "Saint Petersburg"},
      "experience": {"id": "2", "name": "3-6 years"}
    }
  ],
  "pages": 0,
  "per_page": 100,
  "page": 0,
  "found": 500
}
    return response
