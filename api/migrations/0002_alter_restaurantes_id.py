# Generated by Django 3.2.3 on 2021-05-22 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantes',
            name='id',
            field=models.TextField(max_length=256, primary_key=True, serialize=False),
        ),
    ]
