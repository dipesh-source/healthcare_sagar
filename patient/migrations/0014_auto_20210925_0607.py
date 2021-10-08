# Generated by Django 3.2.6 on 2021-09-25 00:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0013_alter_feedback_patint'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='text',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='select',
            field=models.CharField(choices=[('Bad', 'Bad'), ('Average', 'Average'), ('Good', 'Good')], max_length=100),
        ),
    ]
