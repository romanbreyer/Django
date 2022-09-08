from django.urls import path
from .views import reviewer, log_out

urlpatterns = [
    path('', reviewer, name='reviewer'),
    path('logout/', log_out, name='log_out_reviewer'),
]