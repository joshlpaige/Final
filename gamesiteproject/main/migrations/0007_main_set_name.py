# Generated by Django 3.0.6 on 2020-05-18 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200518_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='set_name',
            field=models.TextField(default='-'),
        ),
    ]