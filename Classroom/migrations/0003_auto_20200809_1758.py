# Generated by Django 3.0.8 on 2020-08-09 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Classroom', '0002_auto_20200809_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='message',
            field=models.CharField(max_length=55),
        ),
    ]
