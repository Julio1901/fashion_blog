# Generated by Django 3.1.2 on 2021-01-13 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210113_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to='media'),
        ),
    ]
