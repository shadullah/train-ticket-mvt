from django.urls import path 
from .views import UserReg

urlpatterns = [
    path('register/', UserReg.as_view(), name='register')
]
