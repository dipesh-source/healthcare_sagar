# Generated by Django 3.2.6 on 2021-09-29 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0020_auto_20210929_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_app',
            name='link',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]
