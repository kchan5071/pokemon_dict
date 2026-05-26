import requests
from requests import Response

from enum import Enum

class Base(Enum):
    URL = "https://pokeapi.co/api/v2/"
    TIMEOUT = 10
    GOOD_RESPONSE = 200
    GENERATION = 1

def get_pokemon_info_by_id(dex_id: int) -> Response:
    """
    gets pokemon by dex id
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{dex_id}"
    response = requests.get(url, timeout=Base.TIMEOUT.value)

    if response.status_code == (Base.GOOD_RESPONSE.value):
        data= response.json()
        print(f"Name: {data['name'].capitalize()}")
        print(f"ID: {data['id']}")
        print(f"Height: {data['height']}")
        # List types
        types = [t['type']['name'] for t in data['types']]
        print(f"Types: {', '.join(types)}")
    else:
        print("Pokémon not found!")

    return response

def get_pokemon_info_by_name(name: str) -> Response:
    """
    gets pokemon info by name
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url, timeout=Base.TIMEOUT.value)

    if response.status_code == (Base.GOOD_RESPONSE.value):
        data= response.json()
        print(f"Name: {data['name'].capitalize()}")
        print(f"ID: {data['id']}")
        print(f"Height: {data['height']}")
        # List types
        types = [t['type']['name'] for t in data['types']]
        print(f"Types: {', '.join(types)}")
    else:
        print("Pokémon not found!")

    return response

def get_pokemon_basic_info_batch(
        batch_size: int = 50,
        starting_id: int = 0,

    ) -> Response:
    """Fetch pokemon names by ID in a batch starting from starting_id"""
    url = f"{Base.URL.value}pokemon?limit={batch_size}&offset={starting_id}"
    print("FETCH URL: ", url)
    response = requests.get(url, timeout=Base.TIMEOUT.value)
    if response.status_code == (Base.GOOD_RESPONSE.value):
        return response
    print(f"INVALID RESPONSE: {response.status_code}")
    return response

def main():
    data = get_pokemon_basic_info_batch(50, 5)
    if data is not None:
        print(get_pokemon_basic_info_batch(50, 5).json())

if __name__ == "__main__":
    main()
