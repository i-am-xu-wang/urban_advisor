from django.db import models


# Create your models here.

class Expense(models.Model):
    expenses = models.CharField(max_length=250)
    Roanoke = models.FloatField()
    dc = models.FloatField()
    Philadelphia = models.FloatField()
    Boston = models.FloatField()
    Seattle = models.FloatField()
    sf = models.FloatField()

    def __str__(self):
        return self.expenses
