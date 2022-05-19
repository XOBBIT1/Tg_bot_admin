# Generated by Django 3.2.9 on 2022-05-16 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Massage_bot7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название сообщения')),
                ('massege', models.TextField(verbose_name='Сообщение')),
                ('image', models.ImageField(blank=True, upload_to='avatars')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Время')),
            ],
            options={
                'verbose_name': 'Voronka1',
            },
        ),
        migrations.CreateModel(
            name='MassageVor2_bot7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название сообщения')),
                ('massege', models.TextField(verbose_name='Сообщение')),
                ('image', models.ImageField(blank=True, upload_to='avatars')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Время')),
            ],
            options={
                'verbose_name': 'Voronka2',
            },
        ),
        migrations.CreateModel(
            name='MassageVor3_bot7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название сообщения')),
                ('massege', models.TextField(verbose_name='Сообщение')),
                ('image', models.ImageField(blank=True, upload_to='avatars')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Время')),
            ],
            options={
                'verbose_name': 'Voronka3',
            },
        ),
        migrations.CreateModel(
            name='MassageVor4_bot7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название сообщения')),
                ('massege', models.TextField(verbose_name='Сообщение')),
                ('image', models.ImageField(blank=True, upload_to='avatars')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Время')),
            ],
            options={
                'verbose_name': 'Voronka4',
            },
        ),
        migrations.CreateModel(
            name='MassageVor5_bot7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название сообщения')),
                ('massege', models.TextField(verbose_name='Сообщение')),
                ('image', models.ImageField(blank=True, upload_to='avatars')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Время')),
            ],
            options={
                'verbose_name': 'Voronka5',
            },
        ),
        migrations.CreateModel(
            name='Profile_bot7',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='ID пользователя')),
                ('name', models.TextField(null=True, verbose_name='Имя пользователя')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Время')),
            ],
            options={
                'verbose_name': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='ProfileVor2_bot7',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='ID пользователя')),
                ('name', models.TextField(null=True, verbose_name='Имя пользователя')),
            ],
            options={
                'verbose_name': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='ProfileVor3_bot7',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='ID пользователя')),
                ('name', models.TextField(null=True, verbose_name='Имя пользователя')),
            ],
            options={
                'verbose_name': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='ProfileVor4_bot7',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='ID пользователя')),
                ('name', models.TextField(null=True, verbose_name='Имя пользователя')),
            ],
            options={
                'verbose_name': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='ProfileVor5_bot7',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='ID пользователя')),
                ('name', models.TextField(null=True, verbose_name='Имя пользователя')),
            ],
            options={
                'verbose_name': 'Профили',
            },
        ),
    ]
