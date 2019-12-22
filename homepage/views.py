from django.shortcuts import render

# Create your views here.
# Контроллер-функция, которая возвращает нам базовую страницу из папки шаблонов
def index(request):
    return render(request, 'basic.html')

