# Модуль, содержащий код контроллеров приложения («вьюшек»).
# Так называемыевьюшки» – это функции или классы, получающие запросы пользователей и выполняющие их обработку.

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Accommodation


def main(request):
    # визуализацию обеспечивает функция render()
    return render(request, 'mainapp/index.html')


def accommodations(request):
    title = 'размещение'
    list_of_accommodations = Accommodation.objects.filter(is_active=True)
    # Динамически данные отправленные в шаблон
    # контекст - данные, передаваемые в шаблон динамически
    content = {
        'title': title,
        'list_of_accommodations': list_of_accommodations,
    }
    print("list_of_accommodations ", list_of_accommodations)

    return render(request, 'mainapp/accommodations.html', content)


def accommodation(request, pk):
    title = 'продукты'
    content = {
        'title': title,
        'accommodation': get_object_or_404(Accommodation, pk=pk),
    }
    return render(request, 'mainapp/accommodation_details.html', content)
