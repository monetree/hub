from django.db import models

# Create your models here.

class FibonacciModel(models.Model):
    num = models.BigIntegerField(null= True, blank=True)
    res = models.BigIntegerField(null= True, blank=True)

    def __str__(self):
        return "fibonacci of {} is {}".format(self.num, self.res)
