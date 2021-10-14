from collections import namedtuple

import httpx
from src.settings import API_URL


class SwapiApiConsumer:

    @classmethod
    def get_starships(cls, page: int) -> any:
        with httpx.Client() as client:
            response = client.get(API_URL, params={'page': page})
            response.raise_for_status()

        return response
