# Generated by Django 3.2.6 on 2021-09-13 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0002_station_accessible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='station',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='stop',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
