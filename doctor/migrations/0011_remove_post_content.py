# Generated by Django 3.2.6 on 2021-09-14 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0010_post_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
    ]
