# Generated by Django 3.2.6 on 2021-09-29 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0021_alter_book_app_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_app',
            name='do_this',
        ),
    ]