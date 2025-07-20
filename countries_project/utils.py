import json
# from pathlib import Path
from django.core.exceptions import ImproperlyConfigured

def parse_json_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def process_json_data(filename):
    try:
        data = parse_json_file(filename)
    except FileNotFoundError:
        raise ImproperlyConfigured(f"Файл {filename} не найден в корне проекта.")
    except json.JSONDecodeError as e:
        raise ImproperlyConfigured(f"Ошибка декодирования JSON: {e}")
    except Exception as e:
        raise ImproperlyConfigured(f"Неожиданная ошибка при загрузке JSON: {e}")

    return data

# def process_json_data(filename):
#     data = parse_json_file(filename)
#     return data[0]
#
#
# try:
#     process_json_data(Path("data") / "json_data01.json")
# except FileNotFoundError:
#     print("Файл не найден!")
# except json.JSONDecodeError as e:
#     print(f"Ошибка JSON: {e}")
# except KeyError:
#     print(f"Некорректная обработка данных")
# except BaseException as e:
#     print(e)