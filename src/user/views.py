from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import UserRegisterForm


# Create your views here.
class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('login')
    success_message = "Пользователь %(username)s зарегистрирован"
