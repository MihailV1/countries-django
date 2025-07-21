import json
import logging
from pathlib import Path
from countries.models import Country



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

def load_data_to_db():
    countries_data = process_json_data(Path() / "country-by-languages.json")

    for entry in countries_data:
        country_name = entry['country']
        # language_names = entry['languages']

        # Создаём или получаем страну
        Country.objects.get_or_create(name=country_name)

        # for lang_name in language_names:
        #     language, _ = Language.objects.get_or_create(name=lang_name)
        #     country.languages.add(language)

    print("Данные успешно импортированы в базу.")

