from django.urls import path, include
from .views import index, other_page

app_name = 'homepage'
urlpatterns = [
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]
