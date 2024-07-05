from django.urls import path

from .views import RegisterView, homepage, login_view, logout_view

urlpatterns = [
    path("", homepage, name="homepage"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
