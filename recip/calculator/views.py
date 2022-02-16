from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 153,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def create_count(amount, dict_data):
    _data = {}
    count = int(amount)

    for key, mean in dict_data.items():
        _data[key] = round(mean * count, 3)

    result = {'recipe': _data,
               'count': count}
    return result


def home_view(request):
    contex = {'list_dish': list(DATA)}

    return render(request, 'calculator/menu.html', contex)

def omlet_view(request):
    count = int(request.GET.get('serv', 1))
    context = create_count(count, DATA['omlet'])

    return render(request,'calculator/index.html', context)

def pasta_view(request):
    amount = request.GET.get('serv', 1)
    dish_dict = DATA['pasta']
    context = create_count(amount, dish_dict)

    return render(request, 'calculator/index.html', context)

def buter_view(request):
    amount = request.GET.get('serv', 1)
    context = create_count(amount, DATA['buter'])


    return render(request, 'calculator/index.html', context)