# Generated by Django 3.0.6 on 2020-05-15 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('about', models.TextField()),
                ('abouttxt', models.TextField(default='')),
                ('fb', models.CharField(default='-', max_length=30)),
                ('tw', models.CharField(default='-', max_length=30)),
                ('yt', models.CharField(default='-', max_length=30)),
                ('tell', models.CharField(default='-', max_length=30)),
                ('link', models.CharField(default='-', max_length=30)),
                ('set_name', models.CharField(default='-', max_length=30)),
                ('picurl', models.TextField(default='')),
                ('picname', models.TextField(default='')),
                ('picurl2', models.TextField(default='')),
                ('picname2', models.TextField(default='')),
            ],
        ),
    ]
