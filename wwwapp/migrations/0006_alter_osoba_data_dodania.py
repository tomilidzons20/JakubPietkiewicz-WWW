# Generated by Django 4.2.6 on 2023-11-09 13:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wwwapp', '0005_alter_osoba_plec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateField(default=datetime.date(2023, 11, 9)),
        ),
    ]
