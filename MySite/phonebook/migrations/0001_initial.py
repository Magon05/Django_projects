# Generated by Django 4.1.2 on 2023-03-29 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=60, verbose_name='ФИО')),
                ('phone_number', models.CharField(max_length=40, verbose_name='Номер')),
                ('phone_type', models.CharField(max_length=20)),
                ('comment', models.TextField(verbose_name='Комментарий')),
            ],
        ),
    ]