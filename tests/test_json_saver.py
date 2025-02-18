from src.json_saver import JSONSaver
from src.vacancy import Vacancy


def test_add_vacancy(json_saver: JSONSaver, vacancy_2: Vacancy) -> None:
    """Тест на добавление вакансии"""
    vacancies = json_saver._read_vacancies()
    assert vacancies == []

    json_saver.add_vacancy(vacancy_2)

    vacancies = json_saver._read_vacancies()
    assert len(vacancies) == 1
    assert vacancies[0]["name"] == "Java Developer"
    assert vacancies[0]["salary"] == 80000


def test_add_existing_vacancy(json_saver: JSONSaver, vacancy_2: Vacancy) -> None:
    """Тест на добавление уже существующей вакансии"""
    json_saver.add_vacancy(vacancy_2)

    json_saver.add_vacancy(vacancy_2)

    vacancies = json_saver._read_vacancies()
    assert len(vacancies) == 1


def test_delete_vacancy(json_saver: JSONSaver, vacancy_1: Vacancy) -> None:
    """Тест на удаление вакансии"""
    json_saver.add_vacancy(vacancy_1)

    json_saver.delete_vacancy(vacancy_1)

    vacancies = json_saver._read_vacancies()
    assert vacancies == []


def test_delete_nonexistent_vacancy(json_saver: JSONSaver, vacancy_2: Vacancy) -> None:
    """Тест на попытку удаления несуществующей вакансии"""
    json_saver.delete_vacancy(vacancy_2)

    vacancies = json_saver._read_vacancies()
    assert vacancies == []


def test_read_vacancies_empty_file(json_saver: JSONSaver) -> None:
    """Тест на чтение пустого файла"""
    vacancies = json_saver._read_vacancies()
    assert vacancies == []
