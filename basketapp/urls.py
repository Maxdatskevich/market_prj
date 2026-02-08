from django.urls import path

import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.basket, name='view'),
    path('add/<int:pk>/', basketapp.basket_add, name='add'),
    path('remove/<int:pk>/', basketapp.basket_remove, name='remove'),
    path('edit/<int:pk>/<int:nights>/', basketapp.basket_edit, name='edit'),
]


'''
AJAX - подход, асинхронный 
что такое js AJAX


REST протокол
протокол = соглашения, договоренности
запрос на получение создание изменение удаление
API программный интерфейс обращения куда-то  к сторонним приложениям
Django Rest
работаем по rest протоколу, так же как и http
http протокол
rest набор соглашений и правил
get - просто зайти и получить что-то
post - данные ввести и отправить 
put - изменить
delete - далисть

















'''
