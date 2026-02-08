
from django.urls import path

import authapp.views as authapp
# import authapp.views

app_name = 'authapp'

# Привязка - это выражение, шаблон юрл маршрута + обрабочик
urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('register/', authapp.register, name='register'),
    path('edit/', authapp.edit, name='edit'),
]





#