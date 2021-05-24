# Generated by Django 3.2.3 on 2021-05-22 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurantes',
            fields=[
                ('id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('name', models.TextField()),
                ('site', models.TextField()),
                ('email', models.TextField()),
                ('phone', models.TextField()),
                ('street', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
    ]