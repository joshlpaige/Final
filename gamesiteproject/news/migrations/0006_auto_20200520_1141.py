# Generated by Django 3.0.6 on 2020-05-20 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_news_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='categoryid',
            new_name='catid',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='category',
            new_name='catname',
        ),
    ]