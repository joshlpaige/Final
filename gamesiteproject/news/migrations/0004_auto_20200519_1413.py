# Generated by Django 3.0.6 on 2020-05-19 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200519_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='pic',
            new_name='picname',
        ),
        migrations.AddField(
            model_name='news',
            name='picurl',
            field=models.TextField(default='-'),
        ),
    ]
