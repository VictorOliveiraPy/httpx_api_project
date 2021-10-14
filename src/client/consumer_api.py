import httpx


class SwapiApiCOnsumer:

    @classmethod
    def get_starships(cls, page: int) -> any:
        params = {'page': page}

        with httpx.Client() as client:
            resp = client.get('https://swapi.dev/api/starships/', params=params)

            return resp.json()


