# Generated by Django 4.1 on 2022-08-25 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
