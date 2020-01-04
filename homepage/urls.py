from django.urls import path, include
from .views import index, post_view

app_name = 'homepage'
urlpatterns = [
    path('post/', post_view, name='recent_post'),
    path('', index, name='index'),
]
