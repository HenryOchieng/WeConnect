# Generated by Django 3.1.6 on 2021-04-13 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0014_auto_20210413_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to='profile_pics'),
        ),
    ]