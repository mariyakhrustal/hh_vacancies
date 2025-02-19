from unittest.mock import MagicMock, patch

from src.json_saver import JSONSaver
from src.vacancy_manager import VacancyManager


def test_get_vacancies_by_salary(setup_vacancies: VacancyManager) -> None:
    """Тест на сортировку вакансий по зарплате"""
    manager = setup_vacancies

    result = manager.get_vacancies_by_salary(60000, 120000)
    assert len(result) == 3
    assert result[0].salary == 60000
    assert result[1].salary == 70000


def test_sort_vacancies(setup_vacancies: VacancyManager) -> None:
    """Тест на сортировку вакансий по возрастанию и убыванию"""
    manager = setup_vacancies

    result = manager.sort_vacancies("1")
    assert result[0].salary == 50000
    assert result[3].salary == 80000

    result = manager.sort_vacancies("2")
    assert result[0].salary == 80000
    assert result[3].salary == 50000


def test_get_top_vacancies(setup_vacancies: VacancyManager) -> None:
    """Тест на получение топ n вакансий"""
    manager = setup_vacancies

    result = manager.get_top_vacancies(2)
    assert len(result) == 2
    assert result[0].salary == 80000
    assert result[1].salary == 70000


def test_print_vacancies(setup_vacancies: VacancyManager) -> None:
    """Тест на печать вакансий"""
    manager = setup_vacancies

    result = manager.print_vacancies()
    assert len(result) == 4
    assert "Junior Developer" in result[0]
    assert "Lead Developer" in result[3]

    manager.vacancies_list = []
    result = manager.print_vacancies()
    assert result == ["Нет вакансий для отображения"]


def test_filter_vacancies_no_experience(setup_vacancies: VacancyManager) -> None:
    """Тест на фильтрацию вакансий при отсутствии опыта"""
    manager = setup_vacancies
    none_experience = manager.filter_vacancies(0)
    assert len(none_experience) == 1
    assert none_experience[0].experience == "нет опыта"


def test_filter_vacancies_experience_3(setup_vacancies: VacancyManager) -> None:
    """Тест на фильтрацию вакансий при опыте от 1 года до 3 лет"""
    manager = setup_vacancies
    experience_3 = manager.filter_vacancies(3)
    assert len(experience_3) == 1
    assert experience_3[0].experience == "от 1 года до 3 лет"


def test_filter_vacancies_experience_6(setup_vacancies: VacancyManager) -> None:
    """Тест на фильтрацию вакансий при опыте от 3 до 6 лет"""
    manager = setup_vacancies
    experience_6 = manager.filter_vacancies(6)
    assert len(experience_6) == 1
    assert experience_6[0].experience == "от 3 до 6 лет"


def test_filter_vacancies_experience_10(setup_vacancies: VacancyManager) -> None:
    """Тест на фильтрацию вакансий при опыте более 6 лет"""
    manager = setup_vacancies
    experience_10 = manager.filter_vacancies(10)
    assert len(experience_10) == 1
    assert experience_10[0].experience == "более 6 лет"


def test_add_or_delete_choice_exit(setup_vacancies: VacancyManager) -> None:
    """Тест на выход из программы при вводе неверного значения"""
    manager = setup_vacancies
    assert manager.add_or_delete_choice("3") is None


@patch("builtins.input", return_value="12345")
@patch.object(JSONSaver, "delete_vacancy")
def test_delete_vacancy(
    mock_delete_vacancy: MagicMock, mock_input: MagicMock, setup_vacancies: VacancyManager
) -> None:
    """Тест на вызов метода удаления вакансии при вводе '2'"""
    manager = setup_vacancies
    with patch("builtins.input", return_value="12345"):
        manager.add_or_delete_choice("2")
