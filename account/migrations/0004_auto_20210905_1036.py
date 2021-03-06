# Generated by Django 3.2.6 on 2021-09-05 05:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210904_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeuser',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customeuser',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='customeuser',
            name='mobile',
            field=models.PositiveBigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customeuser',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
