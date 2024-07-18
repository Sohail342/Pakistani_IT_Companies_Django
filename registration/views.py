from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'sign-in.html')


def signup(request):
    return render(request, 'sign-up.html')