from django.db import models

# Create your models here.


class BankruptButton(models.Model):
    bankrupt = models.BooleanField(default=False)


    def __str__(self):
        return f'Bankrupt Button'