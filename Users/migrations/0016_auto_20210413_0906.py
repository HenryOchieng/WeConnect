# Generated by Django 3.1.6 on 2021-04-13 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0015_auto_20210413_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]