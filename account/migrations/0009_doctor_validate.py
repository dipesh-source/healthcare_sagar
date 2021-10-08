# Generated by Django 3.2.6 on 2021-09-17 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20210915_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_validate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(max_length=100)),
                ('mas', models.CharField(blank=True, max_length=100, null=True)),
                ('check', models.BooleanField(default=False)),
            ],
        ),
    ]