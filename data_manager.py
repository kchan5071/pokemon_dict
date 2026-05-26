from requests import Response
from typing import cast

from api.pokeapi_request import (
    get_pokemon_basic_info_batch
)
from cache.cache_manager import CacheTracker
from utils.utils import decode_url_for_id

class DataManager():
    def __init__(self):
        self.cache_tracker = CacheTracker()

    @staticmethod
    def _translate_range_to_index(dex_id: int, id_range: range) -> int:
        new_id = dex_id - id_range.start
        if new_id > 0:
            return new_id
        else:
            return -1
        
    def get_names(self, id_range: range) -> list:
        name_list = []
        dict = self.load(id_range)
        for item in dict.items():
            print(type(item))
            name_list.append(item[1])
        return name_list



           
    def load(self, id_range: range) -> dict:
        # fill from cache
        cached_data, ids_not_in_cache = self.cache_tracker.load_from_cache(
            id_range=id_range
        )
        print(ids_not_in_cache)

        if ids_not_in_cache == [(0, 0)]:
            return cached_data

        # get remaining
        api_data: list[Response] = []
        api_dict = {}
        for api_get_range in ids_not_in_cache:
            if api_get_range == (0, 0):
                continue
            print("BATCH SIZE:", api_get_range[1] - api_get_range[0])
            api_call = get_pokemon_basic_info_batch(
                batch_size=api_get_range[1] - api_get_range[0],
                starting_id=api_get_range[0]
            )
            result_list = api_call.json()["results"]
            print(result_list)
            for result_dict in result_list:
                for result_dict in result_list:
                    self.cache_tracker.cache(result_dict)
                    dex_id = decode_url_for_id(result_dict["url"])
                    api_dict[str(dex_id)] = result_dict

            api_data.append(api_call)

        if api_data == [None]:
            return cached_data

        self.cache_tracker.write_cache_file()
        return cached_data | api_dict
