from tkinter.font import names

from django.http import HttpResponseNotFound
from django.shortcuts import render
from countries_project.utils import process_json_data, get_alphabetical_list
from pathlib import Path
from django.db.models import Count
from countries.models import Country, Language
from django.core.paginator import Paginator
from urllib.parse import unquote #  раскодирует все символы, закодированные в URL-формате.

JSON_FILE_PATH = Path() / "country-by-languages.json"
# Create your views here.

def index_page(request):
    # json
    # countries_data = process_json_data(JSON_FILE_PATH)
    # total_countries = len(countries_data)

    # sqlite
    countries_data = Country.objects.all()
    total_countries = countries_data.count()

    languages_data = Language.objects.all()
    total_languages = languages_data.count()

    top_languages = Language.objects.annotate(country_count=Count("country")).order_by("-country_count")[:5]
    top_countries = Country.objects.annotate(language_count=Count("languages")).order_by("-language_count")[:5]
    # Собираем все языки в один список
    # all_languages = []
    # for country in countries_data:
    #     all_languages.extend(country["languages"])
    #
    # # Убираем дубликаты с помощью set, затем сортируем
    # unique_languages = sorted(set(all_languages))
    # total_languages = len(unique_languages)

    context = {'pagename': 'Country by languages',
               'total_countries': total_countries,
               'total_languages': total_languages,
               "top_languages": top_languages,
               "top_countries": top_countries,
                }
    return render(request, 'pages/index.html', context)

def countries_list_view(request):
    # json
    # countries_data = process_json_data(JSON_FILE_PATH)
    # sqlite
    countries_data = Country.objects.all().order_by('name')
    # print(f"\n\n\n{countries_data}\n\n\n")
    alphabetical_list = get_alphabetical_list(countries_data)

    letter = request.GET.get("letter")
    if letter is not None:
        countries_data = Country.objects.filter(name__istartswith=letter).order_by("name")
        pagename = f'All countries starting with "{letter.upper()}"'
    else:
        pagename = "List of all countries"
    # paginator
    # print(f"\n\n\n\ncountries_data: {countries_data}\n\n\n\n")
    paginator = Paginator(countries_data, 10)  # Показывать по 10 сниппетов на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # Получаем объект Page для запрошенной страницы

    context = {'pagename': pagename,
               'alphabetical_list': alphabetical_list,
               'page_obj': page_obj,
                }
    return render(request,'pages/countries_list.html', context)

def country_detail(request, country_name):
    # json
    # countries_data = process_json_data(JSON_FILE_PATH)
    # sqlite
    countries_data = Country.objects.all()

    country_name = unquote(country_name) #  раскодирует все символы, закодированные в URL-формате.

    # json
    # country_info = next((c for c in countries_data if c["country"] == country_name), None)
    # sqlite
    country_info = next((c for c in countries_data if c.name == country_name), None)

    if country_info is None:
        country_info = {
            # "country": country_name,
            # "languages": [],
            "error": "Дітько! Страна не найдена"
        }
        country_languages = []
    else:
        country_languages = country_info.languages.all()
        country_info = {
            "count": len(country_languages)
        }


    context = {
        'pagename': country_name,
        'languages': country_languages,
        'country_info': country_info,
    }
    return render(request, 'pages/country.html', context)

def languages_list_view(request):
    # json
    countries_data = process_json_data(JSON_FILE_PATH)
    # sqlite
    languages_data = Language.objects.all().order_by('name')
    alphabetical_list = get_alphabetical_list(languages_data)
    # json
    # Собираем все языки в один список
    # all_languages = []
    # for country in countries_data:
    #     all_languages.extend(country["languages"])
    # Убир\аем дубликаты с помощью set, затем сортируем
    # unique_languages = sorted(set(all_languages))
    letter = request.GET.get("letter")
    if letter is not None:
        languages_data = Language.objects.filter(name__istartswith=letter).order_by("name")
        # print(f"\n\n\n\nLetter: {letter}\n\n\n\n")
        pagename = f'All languages starting with "{letter.upper()}"'
    else:
        pagename = "List of all languages"

    # paginator
    paginator = Paginator(languages_data, 10)  # Показывать по 10 сниппетов на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # Получаем объект Page для запрошенной страницы
    # print(f"\nItems on page {page_number}: {list(page_obj)}\n")
    context = {
        'pagename': pagename,
        'alphabetical_list': alphabetical_list,
        'page_obj': page_obj,
    }
    return render(request, 'pages/languages_list.html', context)

def language_detail(request, language_name):
    language_name = unquote(language_name) #  раскодирует все символы, закодированные в URL-формате.
    language_in_countries = Country.objects.filter(languages__name=language_name)
    language_info = {}

    if not language_in_countries:
        language_info = {
            "error": "Дітько! Язык не найден"
        }
        language_in_countries = []
    else:
        language_info = {
            "count": len(language_in_countries)
        }
    context = {
        'pagename': language_name,
        'language_in_countries': language_in_countries,
        'language_info': language_info,
    }
    return render(request, 'pages/language.html', context)