from django.contrib.auth import views
from django.urls import path
from .views import UserRegisterView

urlpatterns = [
    path("login/", views.LoginView.as_view(template_name="user/login.html", extra_context={"title": "Вход"}),
         name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path('register/', UserRegisterView.as_view(), name='register'),
]
