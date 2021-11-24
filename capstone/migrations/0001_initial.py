# Generated by Django 3.2.5 on 2021-11-24 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expenses', models.CharField(max_length=250)),
                ('roanoke', models.FloatField()),
                ('dc', models.FloatField()),
                ('philly', models.FloatField()),
                ('boston', models.FloatField()),
                ('seattle', models.FloatField()),
                ('sf', models.FloatField()),
            ],
        ),
    ]
