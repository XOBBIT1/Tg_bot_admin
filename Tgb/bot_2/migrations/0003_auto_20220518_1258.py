# Generated by Django 3.2.9 on 2022-05-18 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_2', '0002_alter_profile_bot2_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='massage_bot2',
            name='crib',
            field=models.CharField(default=1, max_length=200, verbose_name='Шпаргалка: '),
        ),
        migrations.AddField(
            model_name='massagevor2_bot2',
            name='crib',
            field=models.CharField(default=1, max_length=200, verbose_name='Шпаргалка: '),
        ),
        migrations.AddField(
            model_name='massagevor3_bot2',
            name='crib',
            field=models.CharField(default=1, max_length=200, verbose_name='Шпаргалка: '),
        ),
        migrations.AddField(
            model_name='massagevor4_bot2',
            name='crib',
            field=models.CharField(default=1, max_length=200, verbose_name='Шпаргалка: '),
        ),
        migrations.AddField(
            model_name='massagevor5_bot2',
            name='crib',
            field=models.CharField(default=1, max_length=200, verbose_name='Шпаргалка: '),
        ),
    ]
