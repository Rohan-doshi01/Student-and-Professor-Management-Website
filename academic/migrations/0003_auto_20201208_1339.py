# Generated by Django 3.0.7 on 2020-12-08 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0002_auto_20200128_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classregistration',
            name='department',
            field=models.CharField(choices=[('Science', 'Science'), ('Commerce', 'Commerce'), ('Arts', 'Arts')], max_length=15),
        ),
        migrations.AlterField(
            model_name='classregistration',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
