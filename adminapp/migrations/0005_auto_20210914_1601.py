# Generated by Django 3.2.6 on 2021-09-14 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_auto_20210914_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualified',
            name='fdate',
            field=models.DateTimeField(auto_created=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='qualified',
            name='img',
            field=models.ImageField(upload_to='quali_doc'),
        ),
    ]
