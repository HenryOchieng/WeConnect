# Generated by Django 3.1.6 on 2021-03-10 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0009_auto_20210309_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/media/profile_pics/default_dkL9DSh.png', upload_to='profile_pics'),
        ),
    ]