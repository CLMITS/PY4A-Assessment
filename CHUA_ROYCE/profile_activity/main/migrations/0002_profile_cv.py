# Generated by Django 2.2.1 on 2019-05-26 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cv',
            field=models.FileField(blank=True, upload_to='cv'),
        ),
    ]
