from django.urls import path
from .views import API_Register, API_Login, API_Logout

urlpatterns = [
    path('register/', API_Register, name='register'),
    path('login/', API_Login, name='login'),
    path('logout/', API_Logout, name='logout'),
]