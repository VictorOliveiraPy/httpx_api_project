from src.client.consumer_api import SwapiApiCOnsumer


def test_get_starships():
    api_consumer = SwapiApiCOnsumer()
    resp = api_consumer.get_starships(page=1)

    print(resp)