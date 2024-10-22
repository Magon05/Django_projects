from django.db import models


class Otdelenia(models.Model):

    FIO = models.CharField(max_length=60)
    Dolshnost = models.CharField(max_length=60)
    Otdelenie = models.CharField(max_length=60)
    Telephon = models.TextField(max_length=150)
    Pochta = models.TextField(max_length=150, blank=True)

    def __str__(self):
        return self.FIO

