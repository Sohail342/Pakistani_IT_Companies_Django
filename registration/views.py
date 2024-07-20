from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.urls import reverse


# Create your views here.
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('dashboard'))
    else:
        form  = UserCreationForm()
        
    return render(request, 'sign-up.html', {'form':form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse('dashboard'))
        
    else:
        form  = AuthenticationForm()
    return render(request, 'sign-in.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('Login')

def navbar(request):
    return render(request, 'navbar.html')
