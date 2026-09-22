import json

def safe_to_file(data: list, file_path: str) -> None:
    """
    safe to file in peth
    :param data:
    :param path:
    """
    try:
        with open(file_path, 'w') as data_file:
            json.dump(data, data_file, indent=4)
    except Exception:
        pass