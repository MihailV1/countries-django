import json
import logging
from pathlib import Path
from countries.models import Country, Language
from django.core.management import call_command



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
        language_names = entry['languages']

        # Создаём или получаем страну
        # country = Country.objects.get_or_create(name=country_name)[0]
        # country, created = Country.objects.get_or_create(name=country_name)
        # if created:
        #     print(f"Добавлена новая страна: {country.name}")
        country, _ = Country.objects.get_or_create(name=country_name)

        for lang_name in language_names:
            language, _ = Language.objects.get_or_create(name=lang_name)
            country.languages.add(language)

    print("Данные успешно импортированы в базу.")

def dump_fixture():
    fixtures_path = Path("countries/fixtures")
    fixtures_path.mkdir(parents=True, exist_ok=True)  # Создаёт директорию, если её нет

    try:
        with open(fixtures_path / "countries_all.json", "w", encoding="utf-8") as f:
            call_command("dumpdata", "countries", indent=2, stdout=f)
        print("✅ Фикстура успешно сохранена в 'countries/fixtures/countries_all.json'")
        return True
    except Exception as e:
        print(f"❌ Ошибка при создании фикстуры: {e}")
        return False