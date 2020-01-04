from django.shortcuts import render
from .models import Post
# Create your views here.
# Контроллер-функция, которая возвращает нам базовую страницу из папки шаблонов
def index(request):
    return render(request, 'basic.html',)

def post_view(request):
    posts = Post.objects.all()
    return render(request, 'homepage/product_page.html', context={'posts': posts})


