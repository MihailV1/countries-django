from django.shortcuts import render
from countries_project.utils import process_json_data
from pathlib import Path
from django.core.paginator import Paginator

# Create your views here.

def index_page(request):
    context = {'pagename': 'Country by languages'}
    return render(request, 'pages/index.html', context)

def countries_list(request):
    countries_data = process_json_data(Path() / "country-by-languages.json")

    # paginator
    paginator = Paginator(countries_data, 20)  # Показывать по 10 сниппетов на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # Получаем объект Page для запрошенной страницы

    context = {'pagename': 'Список стран',
               'page_obj': page_obj,
               # 'countries_data': countries_data
                }
    return render(request,'pages/countries_list.html', context)