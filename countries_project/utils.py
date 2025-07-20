import json
import logging
# from pathlib import Path


logger = logging.getLogger(__name__)  # логгер

def parse_json_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def process_json_data(filename):
    data = []
    try:
        data = parse_json_file(filename)
    except FileNotFoundError:
        logger.error(f"Файл {filename} не найден в корне проекта.")
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON: {e}")
    except Exception as e:
        logger.error(f"Неожиданная ошибка при загрузке JSON: {e}")

    return data

