from django.db import models
from django.db.models.aggregates import Max

# Create your models here.

class CardEmployees(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=200)
    phone = models.PositiveIntegerField()
    date_of_birth = models.DateField(auto_created=True)

    def __str__(self):
        return self.name