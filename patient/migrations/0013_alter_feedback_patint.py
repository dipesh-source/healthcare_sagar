# Generated by Django 3.2.6 on 2021-09-25 00:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patient', '0012_book_app_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='patint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]