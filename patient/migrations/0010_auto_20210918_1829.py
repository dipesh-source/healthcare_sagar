# Generated by Django 3.2.6 on 2021-09-18 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0009_auto_20210918_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_app',
            name='disease',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book_app',
            name='write',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
    ]
