# Generated by Django 3.1.2 on 2020-11-20 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20201119_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]