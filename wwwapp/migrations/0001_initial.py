# Generated by Django 4.2.6 on 2023-10-19 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stanowisko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField()),
                ('opis', models.CharField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField()),
                ('nazwisko', models.CharField()),
                ('plec', models.CharField(choices=[('M', 'Mężczyzna'), ('K', 'Kobieta'), ('I', 'Inne')])),
                ('stanowisko', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wwwapp.stanowisko')),
            ],
        ),
    ]
