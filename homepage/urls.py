from django.urls import path, include
from .views import index, contacts, BBLoginView, profile, BBLogoutView, ChangeUserInfoView, \
    BBPasswordChangeView, RegisterUserView, RegisterDoneView, user_activate

app_name = 'homepage'
urlpatterns = [
    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('about/', contacts, name='about'),
    path('', index, name='index'),
]
