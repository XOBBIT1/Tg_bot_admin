# Generated by Django 3.2.9 on 2022-05-14 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Massage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название сообщения')),
                ('massege', models.TextField(verbose_name='Сообщение')),
                ('image', models.ImageField(upload_to='avatars')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Время')),
            ],
            options={
                'verbose_name': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='ID пользователя')),
                ('name', models.TextField(verbose_name='Имя пользователя')),
            ],
            options={
                'verbose_name': 'Профили',
            },
        ),
    ]
