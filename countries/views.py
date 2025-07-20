from django.http import HttpResponseNotFound
from django.shortcuts import render
from countries_project.utils import process_json_data
from pathlib import Path
from django.core.paginator import Paginator
from urllib.parse import unquote #  раскодирует все символы, закодированные в URL-формате.

# Create your views here.

def index_page(request):
    context = {'pagename': 'Country by languages'}
    return render(request, 'pages/index.html', context)

def countries_list_view(request):
    countries_data = process_json_data(Path() / "country-by-languages.json")

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
    countries_data = process_json_data(Path() / "country-by-languages.json")
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