from django.contrib.auth import login, logout
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm, LoginForm


def homepage(request):
    return render(request, "registration/homepage.html")


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("homepage")
    template_name = "registration/registration.html"

    def form_valid(self, form):
        to_return = super().form_valid(form)
        login(self.request, self.object)
        return to_return


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("homepage")
    else:
        form = LoginForm()
    return render(request, "registration/login.html", context={"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")
