from src.client.consumer_api import SwapiApiCOnsumer


def test_get_starships(requests_mock):
    requests_mock.get('https://swapi.dev/api/starships/', status_code=200, json={'some': 'thing'})

    api_consumer = SwapiApiCOnsumer()
    resp = api_consumer.get_starships(page=1)

    print(resp)