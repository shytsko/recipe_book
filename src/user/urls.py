from django.contrib.auth import views
from django.urls import path

urlpatterns = [
    path("login/", views.LoginView.as_view(template_name="user/login.html", extra_context={"title": "Вход"}),
         name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]

