# Generated by Django 4.2 on 2023-04-06 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0004_alter_training_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='description',
            field=models.TextField(default='', verbose_name='Açıklama'),
        ),
    ]
