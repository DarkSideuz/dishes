# Generated by Django 5.1.2 on 2024-12-29 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
