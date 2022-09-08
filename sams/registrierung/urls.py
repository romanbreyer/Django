from django.urls import path
from .views import registrierung

urlpatterns = [
    path('', registrierung, name='registrierung'),
]
