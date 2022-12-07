# Generated by Django 3.0.9 on 2020-08-24 17:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20200821_1918'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={},
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(blank=True, default=datetime.date.today, help_text='Введите дату рождения', null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(blank=True, default=datetime.date.today, help_text='Введите дату смерти', null=True, verbose_name='Дата смерти'),
        ),
    ]