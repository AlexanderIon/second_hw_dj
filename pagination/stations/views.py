from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

import csv

from pagination.settings import BUS_STATION_CSV


def get_content(path_file_csv):
    list_content = []

    with open(path_file_csv, 'r', encoding='utf-8') as file:
        reader_dict = csv.DictReader(file)
        for row in reader_dict:
            list_content.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
    return list_content


def index(request):
    return redirect(reverse('bus_stations'))


list_station = get_content(BUS_STATION_CSV)


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))

    paginator = Paginator(list_station, 7)
    name_stations_on_page = paginator.get_page(page_number)

    context = {
         'bus_stations': name_stations_on_page,
         'page': name_stations_on_page,
    }



    return render(request, 'stations/index.html', context)


