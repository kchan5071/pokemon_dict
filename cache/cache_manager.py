
"""
    loads cache
    read from cache
    gets indecies NOT in cache
    writes back to cache
"""

from pathlib import Path
import json
from typing import List, Tuple, Dict
from itertools import groupby
from operator import itemgetter
from json import JSONDecodeError

from utils.utils import (
    decode_url_for_id,
    decode_path_for_name
)

# DICT_FORMAT = {"id": {"api_url", "local_file_path"}}
DICT_FORMAT: Dict[int, Dict[str, str]] = {}
CACHE_FILE_NAME = "cache.json"

class CacheTracker:
    def __init__(self):
        self.current_dir = Path(__file__).resolve().parent
        self.cache_file_path = self.current_dir.joinpath(CACHE_FILE_NAME)
        if self.cache_file_path != self.current_dir:
            self.cache_data:dict = self._read_cache_file()
        else:
            self.cache_data = {}

        
    def _read_cache_file(self) -> dict:
        try:
            with open(self.cache_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                print(data)
            return data
        except FileNotFoundError as e:
            print("FILE NOT FOUND", e)
            return {}
        except JSONDecodeError as e:
            print("FILE EMPTY", e)
            return {}

    def write_cache_file(self):
        # Read the file with duplicates
        try:
            with open(self.cache_file_path, 'r', encoding="utf-8") as file:
                data = json.load(file)
        except JSONDecodeError as e:
            print("FILE EMPTY", e)
            data = {}

        data_to_write = data | self.cache_data

        with open(self.cache_file_path, 'w', encoding="utf-8") as f:
            json.dump(data_to_write, f, indent=4)

    def _check_cache(self, pokemon_id: int):
        check = str(pokemon_id) in self.cache_data
        return check

    def _get_data_by_id(self, dex_id: int):
        return self.cache_data[str(dex_id)]


    def cache(self, to_cache_dict: dict) -> None:
        api_url = to_cache_dict["url"]
        local_file_path =  self.current_dir.joinpath(to_cache_dict["name"])
        dex_id = decode_url_for_id(api_url)
        new_cache_entry = {
            dex_id: {
                "api_url": api_url,
                "local_file_path": str(local_file_path),
                "name": to_cache_dict["name"]
            }
        }
        self.cache_data.update(new_cache_entry)

        

    def load_from_cache(self, id_range: range) -> Tuple[dict, List[range]]:
        # create list of cache misses
        cache_misses = []
        data_dict = {}
        # iterate through dex_ids and creates list of data and cache misses
        for dex_id in id_range:
            if (self._check_cache(dex_id)):
                data_dict[str(dex_id)] = (self._get_data_by_id(
                    dex_id=dex_id
                ))
            else:
                cache_misses.append(dex_id)


        # group consecutive together
        cache_ranges = []
        for _, g in groupby(enumerate(cache_misses), lambda x: x[0] - x[1]):
            group = list(map(itemgetter(1), g))
            cache_ranges.append((group[0], group[-1]))

        return data_dict, cache_ranges

