from unittest.mock import patch, Mock, MagicMock

from requests import RequestException

from src.head_hunter_api import HeadHunterAPI


@patch('requests.get')
def test_connect_to_api(mock_get: MagicMock) -> None:
    """Тест на работу метода подключения к api"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": []}
    mock_get.return_value = mock_response

    api = HeadHunterAPI()
    result = api._connect_to_api(api._HeadHunterAPI__params)

    assert result == {"items": []}
    mock_get.assert_called_once_with('https://api.hh.ru/vacancies', params=api._HeadHunterAPI__params)


@patch('requests.get')
def test_connect_to_api_error(mock_get: MagicMock) -> None:
    """Тест на поведение метода при подключении к api с ошибочным статус кодом"""
    mock_response = Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response

    api = HeadHunterAPI()
    result = api._connect_to_api(api._HeadHunterAPI__params)

    assert result == []
    mock_get.assert_called_once_with('https://api.hh.ru/vacancies', params=api._HeadHunterAPI__params)


@patch('requests.get')
def test_connect_to_api_exception(mock_get: MagicMock) -> None:
    """Тест на выброс исключения при подключении к api"""
    mock_get.side_effect = RequestException("Ошибка соединения")

    api = HeadHunterAPI()
    result = api._connect_to_api(api._HeadHunterAPI__params)

    assert result == []


def test_load_vacancies(json_response_200: dict) -> None:
    """Тест на работу метода для загрузки вакансий"""
    api = HeadHunterAPI()

    api._connect_to_api = Mock(return_value=json_response_200)

    keyword = "Python Developer"
    vacancies = api.load_vacancies(keyword)

    assert len(vacancies) == 2
    assert vacancies[0]["name"] == "Python Developer"
    assert vacancies[1]["salary"] == 2000
    assert vacancies[1]["experience"] == "3-6 years"
    assert vacancies[0]["url"] == "https://hh.ru/vacancy/1234567"


@patch('requests.get')
def test_load_vacancies_error(mock_get: MagicMock) -> None:
    """Тест метода загрузки вакансий в случае неверных данных"""
    mock_response = Mock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response

    api = HeadHunterAPI()
    result = api.load_vacancies("Python Developer")

    assert result == []
    mock_get.assert_called_once_with('https://api.hh.ru/vacancies', params=api._HeadHunterAPI__params)
