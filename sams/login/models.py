"""
Models for login
"""
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Applicant user with data necessary for application
    """
    is_student = models.BooleanField(default=True)
    is_reviewer = models.BooleanField(default=False)
    note = models.FloatField(default=4.0)
    auslandserfahrung = models.BooleanField(default=False)
    empfehlungsschreiben = models.FileField(upload_to='recommendationletters',
                                            default= None,
                                            null=True,
                                            blank=True
                                            )
    abschluss = models.CharField(max_length=15, null=True, blank=True)
