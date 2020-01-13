from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
# Контроллер-функция, которая возвращает нам базовую страницу из папки шаблонов


def index(request):
    return render(request, 'basic.html',)


def contacts(request):
    return render(request, 'homepage/about.html',)

class BBLoginView(LoginView):
    template_name = 'homepage/profile_tmp/login.html'

@login_required
def profile(request):
    return render(request, 'homepage/profile_tmp/profile.html')

class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'homepage/profile_tmp/logout.html'

