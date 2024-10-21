# Generated by Django 5.0.4 on 2024-09-30 12:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0019_alter_product_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])]),
        ),
    ]