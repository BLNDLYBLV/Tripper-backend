# Generated by Django 3.2.3 on 2021-10-19 19:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20211019_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='x',
            field=models.ManyToManyField(related_name='_user_userprofile_x_+', to=settings.AUTH_USER_MODEL),
        ),
    ]