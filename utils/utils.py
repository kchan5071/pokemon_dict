


def translate_range_to_index(dex_id: int, id_range: range) -> int:
    new_id = dex_id - id_range.start
    if new_id > 0:
        return new_id
    else:
        return -1

def decode_url_for_id(url: str) -> int:
    return int(url.rstrip("/").split("/")[-1])

def decode_path_for_name(path: str) -> str:
    return path.rstrip("/").split("/")[-1]