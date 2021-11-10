from django.db import models


# Create your models here.

class Expense(models.Model):
    expenses = models.CharField(max_length=200)
    roanoke = models.IntegerField()
    dc = models.IntegerField()
    philly = models.IntegerField()
    boston = models.IntegerField()
    seattle = models.IntegerField()
    sf = models.IntegerField()

    def __str__(self):
        return self.expenses
