from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import resolve_url
from django.views import View
from django.shortcuts import redirect, render

from main.forms.login_form import LoginForm


# User login view
def UserLoginView(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    context = {'form': forms}
    return render(request, 'auth/new_login.html', context)


def LogoutView(request):
    logout(request)
    return redirect('login')


def Dashboard(request):
    return render(request, 'dashboard/dashboard.html')