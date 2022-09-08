"""
Models for applicant
"""
import math
from django.db import models
from login.models import User

class Application(models.Model):
    """
    Application with status and applying user
    """
    status = models.IntegerField(default=0) # 0 = In Bearbeitung ; 1 = Angenommen ; 2 = Abgelehnt
    applicant = models.OneToOneField(User, on_delete=models.CASCADE)
    @property
    def score(self):
        """
        Calculates the score of an Application
        """
        result = self.applicant.note

        if self.applicant.auslandserfahrung is True:
            result += 1.0
        else:
            result += 2.0

        if self.applicant.empfehlungsschreiben is not None:
            result += 1.0
        else:
            result += 2.0

        if self.applicant.abschluss == 'abitur':
            result += 1.0
        if self.applicant.abschluss == 'fachabitur':
            result += 2.0
        if self.applicant.abschluss == 'ausbildung':
            result += 3.0
        if self.applicant.abschluss == 'keinabschluss':
            result += 4.0
        result = result / 4

        return math.floor(result * 100) / 100.0
