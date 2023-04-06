# Generated by Django 4.2 on 2023-04-06 19:38

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0005_staff_projectname'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingDefinition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainingName', models.CharField(default='', max_length=200, verbose_name='Eğitim Adı')),
                ('trainingdesc', models.TextField(default='', max_length=200, verbose_name='Eğitim Açıklaması')),
                ('preparedTraining', models.CharField(default='', max_length=200, verbose_name='Eğitimi Hazırlayan')),
                ('preparationDate', models.DateField(default=datetime.date.today, verbose_name='Hazırlama tarihi')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('providingTraining', models.CharField(default='', max_length=200, verbose_name='Eğitimi Veren')),
                ('trainingStartDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Eğitim Başlama Tairihi')),
                ('trainingEndDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Eğitim Bitiş Tarihi')),
                ('trainingTime', models.CharField(default='', max_length=100, verbose_name='Eğitim Süresi')),
                ('trainingStatus', models.CharField(choices=[('PLANLANDI', 'Planlandı'), ('GERCEKLESTI', 'Gerçekleşti'), ('BASLADI', 'Başladı'), ('DEVAMEDIYOR', 'Devam Ediyor')], default='', max_length=50, verbose_name='Eğitim Durumu')),
                ('description', models.TextField(default='', verbose_name='Açıklama')),
                ('participants', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='staff.staff', verbose_name='Katılımcılar')),
                ('projectName', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='staff.project', verbose_name='Proje')),
                ('trainingName', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='training.trainingdefinition', verbose_name='Eğitim')),
            ],
        ),
    ]
