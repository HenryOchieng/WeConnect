# Generated by Django 3.1.6 on 2021-03-09 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='Media/default.jpg', upload_to='profile_pics'),
        ),
    ]
