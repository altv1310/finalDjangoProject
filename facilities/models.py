from django.db import models


# Create your models here.
class Facilities(models.Model):
    UF = 'UF'
    RD = 'RD'
    TYPE_CHOICES = [
        (UF, 'User Facility'),
        (RD, 'R&D Agreements for Facility Access')
    ]
    laboratory_name = models.CharField(max_length=80)
    facility = models.CharField(max_length=300)
    address = models.CharField(max_length=80, null=True)
    zip_code = models.CharField(max_length=5, null=True)
    city = models.CharField(max_length=80, null=True)
    state = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=40, null=True)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, null=True)
    link = models.URLField(null=True)
    poc_email = models.EmailField(null=True)
    poc_phone = models.CharField(max_length=40, null=True)

    def __str__(self):
        return f'{self.laboratory_name} {self.facility}'

    @staticmethod
    def get_absolute_url():
        return '/facilitieslist'
