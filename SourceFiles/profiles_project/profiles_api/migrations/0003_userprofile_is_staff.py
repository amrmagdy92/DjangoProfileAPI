# Generated by Django 2.2.4 on 2019-08-24 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_remove_userprofile_isstaff'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
