# Generated by Django 2.1 on 2023-08-06 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='portfolio_site',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
