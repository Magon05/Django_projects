from django.db import models
from django.urls import reverse


class PhoneType(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type


class Person(models.Model):
    full_name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=40)
    phone_type = models.ForeignKey(PhoneType, on_delete=models.PROTECT)
    comment = models.TextField()

    #def get_absolute_url(self):
        #return reverse('books:detail', args=[self.id])


#class Passwords(models.Model):
    #username = models.CharField(max_length=50)
    #password = models.CharField(max_length=50)


