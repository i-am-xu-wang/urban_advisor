# Generated by Django 3.2.5 on 2021-11-10 04:01

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
                ('expenses', models.CharField(max_length=200)),
                ('roanoke', models.IntegerField()),
                ('dc', models.IntegerField()),
                ('philly', models.IntegerField()),
                ('boston', models.IntegerField()),
                ('seattle', models.IntegerField()),
                ('sf', models.IntegerField()),
            ],
        ),
    ]
