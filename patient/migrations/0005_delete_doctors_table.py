# Generated by Django 3.2.6 on 2021-09-18 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_doctors_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Doctors_table',
        ),
    ]
