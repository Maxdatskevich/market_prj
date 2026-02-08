from django.urls import path
import mainapp.views as mainapp

# указать название приложеня
app_name = 'mainapp'


urlpatterns = [
    path('', mainapp.accommodations, name='index'),
    path('accommodation_details/<int:pk>/', mainapp.accommodation,
         name='accommodation'),
]


















