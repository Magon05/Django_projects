# Generated by Django 5.0.4 on 2024-09-24 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0012_alter_product_category_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]