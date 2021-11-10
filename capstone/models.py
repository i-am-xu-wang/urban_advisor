from django.db import models


# Create your models here.

class Expense(models.Model):
    expenses = models.CharField(max_length=250)
    roanoke = models.FloatField()
    dc = models.FloatField()
    philly = models.FloatField()
    boston = models.FloatField()
    seattle = models.FloatField()
    sf = models.FloatField()

    def __str__(self):
        return self.expenses
