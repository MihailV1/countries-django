from django.http import HttpResponseNotFound
from django.shortcuts import render
from countries_project.utils import process_json_data
from pathlib import Path
from django.core.paginator import Paginator
from urllib.parse import unquote #  раскодирует все символы, закодированные в URL-формате.

JSON_FILE_PATH = Path() / "country-by-languages.json"
# Create your views here.

def index_page(request):
    countries_data = process_json_data(JSON_FILE_PATH)
    total_countries = len(countries_data)
    # Собираем все языки в один список
    all_languages = []
    for country in countries_data:
        all_languages.extend(country["languages"])

    # Убираем дубликаты с помощью set, затем сортируем
    unique_languages = sorted(set(all_languages))
    total_languages = len(unique_languages)

    context = {'pagename': 'Country by languages',
               'total_countries': total_countries,
               'total_languages': total_languages}
    return render(request, 'pages/index.html', context)

def countries_list_view(request):
    countries_data = process_json_data(JSON_FILE_PATH)

    # paginator
    paginator = Paginator(countries_data, 20)  # Показывать по 10 сниппетов на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # Получаем объект Page для запрошенной страницы

    context = {'pagename': 'List of countries',
               'page_obj': page_obj,
               # 'countries_data': countries_data
                }
    return render(request,'pages/countries_list.html', context)

def country_detail(request, country_name):
    countries_data = process_json_data(JSON_FILE_PATH)

    country_name = unquote(country_name) #  раскодирует все символы, закодированные в URL-формате.
    country_info = next((c for c in countries_data if c["country"] == country_name), None)
    # print(f"\n{country_info}\n")
    if country_info is None:
        country_info = {
            "country": country_name,
            "languages": [],
            "error": "Дітько! Страна не найдена"
        }

    context = {
        'pagename': country_name,
        'languages': country_info["languages"],
        'country_info': country_info,
    }
    return render(request, 'pages/country.html', context)

def languages_list_view(request):
    countries_data = process_json_data(JSON_FILE_PATH)

    # Собираем все языки в один список
    all_languages = []
    for country in countries_data:
        all_languages.extend(country["languages"])

    # Убираем дубликаты с помощью set, затем сортируем
    unique_languages = sorted(set(all_languages))

    # paginator
    paginator = Paginator(unique_languages, 20)  # Показывать по 10 сниппетов на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # Получаем объект Page для запрошенной страницы
    # print(f"\nItems on page {page_number}: {list(page_obj)}\n")
    context = {
        'pagename': 'Languages',
        'page_obj': page_obj,
    }
    return render(request, 'pages/languages_list.html', context)