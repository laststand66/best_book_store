from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.core.signing import BadSignature


from .models import MainUser
from .forms import ChangeUserInfoForm, RegisterUserForm
from .utilities import signer
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

class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = MainUser
    template_name = 'homepage/profile_tmp/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('homepage:profile')
    success_message = 'Личные данные пользователя изменены'

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class BBPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'homepage/profile_tmp/password_change.html'
    success_url = reverse_lazy('homepage:profile')
    success_message = 'Пароль изменён успешно'


class RegisterUserView(CreateView):
    models = MainUser
    template_name = 'homepage/profile_tmp/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('homepage:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'homepage/profile_tmp/register_done.html'

def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'homepage/user_activation/bad_signature.html')
    user = get_object_or_404(MainUser, username=username)
    if user.is_activated:
        template = 'homepage/user_activation/user_is_activated.html'
    else:
        template = 'homepage/user_activation/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)