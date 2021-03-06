# Generated by Django 3.2.6 on 2021-09-29 13:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0019_alter_book_app_disease'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_app',
            name='do_this',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='do_this'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book_app',
            name='five',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='book_app',
            name='four',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book_app',
            name='link',
            field=models.URLField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book_app',
            name='one',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book_app',
            name='three',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book_app',
            name='two',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
