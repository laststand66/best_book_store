from django.urls import path, include
from .views import index, contacts, BBLoginView, profile, BBLogoutView

app_name = 'homepage'
urlpatterns = [
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('about/', contacts, name='about'),
    path('', index, name='index'),
]
