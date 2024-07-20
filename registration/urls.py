from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='Login'),
    path('signup/', views.signup_view, name='Signup'),
    path('logout/', views.logout_view, name='logout'),
]
