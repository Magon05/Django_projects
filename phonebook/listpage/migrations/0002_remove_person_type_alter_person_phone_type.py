# Generated by Django 4.1 on 2022-10-14 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listpage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='type',
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='listpage.phonetype'),
        ),
    ]