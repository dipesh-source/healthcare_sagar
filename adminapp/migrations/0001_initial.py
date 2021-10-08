# Generated by Django 3.2.6 on 2021-09-04 16:45

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(max_length=100)),
                ('data', froala_editor.fields.FroalaField()),
                ('content', froala_editor.fields.FroalaField()),
                ('fdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
