# Generated by Django 4.2 on 2023-04-05 21:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, verbose_name='Adı')),
                ('surname', models.CharField(default='', max_length=200, verbose_name='Soyadı')),
                ('idNumber', models.PositiveIntegerField(default=False, verbose_name='TC Kimlik No')),
                ('dateofBirth', models.DateField(verbose_name='Doğum Tarihi')),
                ('title', models.CharField(default='', max_length=250, verbose_name='Ünvan')),
                ('phoneNumber', models.CharField(default='', max_length=21, verbose_name='Cep Tel')),
                ('emergencyPhoneNumber', models.CharField(default='', max_length=21, verbose_name='Acil Durumda Aranacak Kişi Tel')),
                ('email', models.EmailField(default='', max_length=50, verbose_name='E-Posta')),
                ('adress', models.TextField(default='', verbose_name='Adres')),
                ('county', models.CharField(default='', max_length=200, verbose_name='İl')),
                ('district', models.CharField(default='', max_length=200, verbose_name='İlçe')),
                ('description', models.TextField(default='', verbose_name='Açıklama')),
                ('dateEntry', models.DateField(default=datetime.date, verbose_name='DD.MM:YYYY')),
                ('releaseDate', models.DateField(default=datetime.date, verbose_name='DD.MM:YYYY')),
                ('bloodgroup', models.CharField(choices=[('0', '0 Rh(-)'), ('00', '0 Rh(+)'), ('A', 'A Rh(-)'), ('AA', 'A Rh(+)'), ('B', 'B Rh(-)'), ('BB', 'B Rh(+)'), ('AB', 'AB Rh(-'), ('AABB', 'AB Rh(+)')], default='', max_length=10, verbose_name='Kan Grubu')),
                ('is_active', models.BooleanField(default=False, verbose_name='Aktif')),
            ],
        ),
    ]