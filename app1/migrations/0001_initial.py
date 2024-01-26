# Generated by Django 5.0.1 on 2024-01-26 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gympaln',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='memeber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('phonenumber', models.IntegerField()),
                ('date', models.DateField()),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.gympaln')),
            ],
        ),
    ]
