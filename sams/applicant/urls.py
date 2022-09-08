from django.urls import path
from .views import applicant, bewerben, daten, log_out

urlpatterns = [
    path('', applicant, name='applicant'),
    path('bewerben/', bewerben, name='bewerben'),
    path('daten/', daten, name='daten'),
    path('logout/', log_out, name='logout_applicant'),
]
