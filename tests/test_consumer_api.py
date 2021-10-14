import httpx

from src.infra.consumer_api import SwapiApiConsumer
from http import HTTPStatus

from src.settings import API_URL


def test_get_starships(requests_mock):
    # requests_mock.get('https://swapi.dev/api/starships/', status_code=200, json={'some': 'thing'})

    api_consumer = SwapiApiConsumer()
    resp = api_consumer.get_starships(page=1)
    assert resp.status_code == httpx.codes.OK
    assert resp.request.method == 'GET'

    print(resp)
