# Generated by Django 4.2 on 2023-04-06 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0008_alter_staff_idnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='idNumber',
            field=models.PositiveIntegerField(default=False, verbose_name='TC Kimlik No'),
        ),
    ]