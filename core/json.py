import json
import os


def read_json(file_path):
    """
    Read a JSON file.

    Args:
        file_path: path to the JSON file

    Returns:
        parsed data (dict or list)

    If file is missing, returns None.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return None


def write_json(file_path, data, indent=2):
    """
    Write data to a JSON file.

    Args:
        file_path: where to write the file
        data: dictionary or list
        indent: formatting indentation (default: 2)

    Creates parent directories if needed.
    """
    dir_name = os.path.dirname(file_path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=indent, ensure_ascii=False)
