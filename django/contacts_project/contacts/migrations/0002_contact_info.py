# Generated by Django 3.1.2 on 2020-11-14 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='info',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
