# Generated by Django 2.1.2 on 2018-10-06 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='price',
            field=models.IntegerField(default=2000),
        ),
    ]