# Generated by Django 3.2.3 on 2021-05-23 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210522_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantes',
            name='lat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='restaurantes',
            name='lng',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='restaurantes',
            name='rating',
            field=models.IntegerField(),
        ),
    ]