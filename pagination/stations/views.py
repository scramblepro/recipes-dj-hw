import csv
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # Открываем CSV-файл с остановками
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        bus_stations = list(reader)  # Читаем все строки в список

    # Используем пагинацию Django
    page_number = request.GET.get('page', 1)  # Получаем текущую страницу, по умолчанию 1
    paginator = Paginator(bus_stations, 10)  # Разбиваем список на страницы по 10 элементов

    page = paginator.get_page(page_number)  # Получаем данные для текущей страницы

    # Формируем контекст для шаблона
    context = {
        'bus_stations': page.object_list,  # Список остановок для текущей страницы
        'page': page,  # Объект страницы для вывода навигации по страницам
    }

    # Рендерим страницу с остановками
    return render(request, 'stations/index.html', context)