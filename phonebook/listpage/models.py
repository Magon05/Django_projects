from django.db import models
from django.urls import reverse


class PhoneType(models.Model):

    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type


class Person(models.Model):

    full_name = models.CharField(max_length=60, verbose_name='ФИО')
    phone_number = models.CharField(max_length=40, verbose_name='Номер')
    phone_type = models.ForeignKey(PhoneType, on_delete=models.PROTECT, verbose_name='Тип телефона')
    comment = models.TextField(verbose_name='Комментарий')
    #datetime_created = models.DateTimeField(auto_now_add=True, editable=False)

    #def get_absolute_url(self):
        #return reverse('books:detail', args=[self.id])


#class Passwords(models.Model):
    #username = models.CharField(max_length=50)
    #password = models.CharField(max_length=50)
"""
class University(models.Model):
    UNIVERSITY_TYPE = ( # new
        ('PUBLIC', 'A public university'),
        ('PRIVATE', 'A private university')
      )

    full_name = models.CharField(
        verbose_name='university full name',
      max_length=100
    )
    university_type = models.CharField( # new
        choices=UNIVERSITY_TYPE_CHOICES,
        max_length=1,
        verbose_name='type of university',
    )

    class Meta:  
        indexes = [models.Index(fields=['full_name'])]
        ordering = ['-full_name']
        verbose_name = 'university'
        verbose_name_plural = 'universities'

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('university_detail', args=[str(self.id)])
"""
"""
class University(models.Model):
    full_name = models.CharField(
        max_length=100,
        verbose_name='university full name',
    )

    class Meta: # new
        indexes = [models.Index(fields=['full_name'])]
        ordering = ['-full_name']
        verbose_name = 'university'
        verbose_name_plural = 'universities'

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('university_detail', args=[str(self.id)])


class Student(models.Model):
    first_name = models.CharField('first name', max_length=30)
    last_name = models.CharField('last name', max_length=30)
    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
        related_name='students',
        related_query_name='person',
    )

    class Meta: # new
        verbose_name = 'student'
        verbose_name_plural = 'students'

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('student_detail', args=[str(self.id)])
"""