from django.db import models
from django.utils.safestring import mark_safe


class Profile_bot9(models.Model):
    id = models.PositiveIntegerField(verbose_name="ID пользователя", primary_key=True, unique=True)
    name = models.TextField(verbose_name="Имя пользователя", null=True, blank=False)
    data = models.DateTimeField(verbose_name="Время", auto_now_add=True)

    def __str__(self):
        return f'Сообщение{self.pk}'


    class Meta:
        verbose_name = "Профили_Воронки_1"


class Massage_bot9(models.Model):
    name = models.CharField(verbose_name="Название сообщения", null=False, blank=False, max_length=200, )
    massege = models.TextField(verbose_name="Сообщение", null=False, blank=False)
    image = models.ImageField(upload_to="avatars", blank=True,)
    data = models.DateTimeField(verbose_name="Время",auto_now_add=True)
    crib = models.CharField(
        "Шпаргалка:\n Воронка 1 : 1./start 2./go 3./ok 4./mes4 5./mes5 6./mes6 7./mes7  8./mes8  9./mes9  10./mes10 "
        "\nВоронка 2 : 2./Vor2_mes2 3./Vor2_mes3 4./Vor2_mes4 5./Vor2_mes5 6./Vor2_mes6 7./Vor2_mes7  8./Vor2_mes8  9./Vor2_mes9 10./Vor2_mes10"
        "\nВоронка 3 : 2./Vor3_mes2 3./Vor3_mes3 4./Vor3_mes4 5./Vor3_mes5 6./Vor3_mes6 7./Vor3_mes7 8./Vor3_mes8 9./Vor3_mes9 10./Vor3_mes10"
        "\nВоронка 4 : 2./Vor4_mes2 3./Vor4_mes3 4./Vor4_mes4 5./Vor4_mes5 6./Vor4_mes6 7./Vor4_mes7 8./Vor4_mes8 9./Vor4_mes9 10./Vor4_mes10"
        "\nВоронка 5 :  2./Vor5_mes2 3./Vor5_mes3 4./Vor5_mes4 5./Vor5_mes5 6./Vor5_mes6 7./Vor5_mes7 8./Vor5_mes8 9./Vor5_mes9 10./Vor5_mes10 ",
        max_length=200, default=1)

    def __str__(self):
        return f'{self.massege}'


    class Meta:
        verbose_name="Voronka1"


class ProfileVor2_bot9(models.Model):
    id = models.PositiveIntegerField(verbose_name="ID пользователя", primary_key=True, unique=True)
    name = models.TextField(verbose_name="Имя пользователя", null=True, blank=False)

    def __str__(self):
        return f'Сообщение{self.pk}'

    class Meta:
        verbose_name = "Профили_Воронки_2"


class MassageVor2_bot9(models.Model):
    name = models.CharField(verbose_name="Название сообщения", null=False, blank=False, max_length=200, )
    massege = models.TextField(verbose_name="Сообщение", null=False, blank=False)
    image = models.ImageField(upload_to="avatars", blank=True,)
    data = models.DateTimeField(verbose_name="Время",auto_now_add=True)
    crib = models.CharField(
        "Шпаргалка:\n Воронка 1 : 1./start 2./go 3./ok 4./mes4 5./mes5 6./mes6 7./mes7  8./mes8  9./mes9  10./mes10 "
        "\nВоронка 2 : 2./Vor2_mes2 3./Vor2_mes3 4./Vor2_mes4 5./Vor2_mes5 6./Vor2_mes6 7./Vor2_mes7  8./Vor2_mes8  9./Vor2_mes9 10./Vor2_mes10"
        "\nВоронка 3 : 2./Vor3_mes2 3./Vor3_mes3 4./Vor3_mes4 5./Vor3_mes5 6./Vor3_mes6 7./Vor3_mes7 8./Vor3_mes8 9./Vor3_mes9 10./Vor3_mes10"
        "\nВоронка 4 : 2./Vor4_mes2 3./Vor4_mes3 4./Vor4_mes4 5./Vor4_mes5 6./Vor4_mes6 7./Vor4_mes7 8./Vor4_mes8 9./Vor4_mes9 10./Vor4_mes10"
        "\nВоронка 5 :  2./Vor5_mes2 3./Vor5_mes3 4./Vor5_mes4 5./Vor5_mes5 6./Vor5_mes6 7./Vor5_mes7 8./Vor5_mes8 9./Vor5_mes9 10./Vor5_mes10 ",
        max_length=200, default=1)

    def __str__(self):
        return f'{self.massege}'


    class Meta:
        verbose_name="Voronka2"


class ProfileVor3_bot9(models.Model):
    id = models.PositiveIntegerField(verbose_name="ID пользователя", primary_key=True, unique=True)
    name = models.TextField(verbose_name="Имя пользователя", null=True, blank=False)

    def __str__(self):
        return f'Сообщение{self.pk}'

    class Meta:
        verbose_name = "Профили_Воронки_3"


class MassageVor3_bot9(models.Model):
    name = models.CharField(verbose_name="Название сообщения", null=False, blank=False, max_length=200, )
    massege = models.TextField(verbose_name="Сообщение", null=False, blank=False)
    image = models.ImageField(upload_to="avatars", blank=True,)
    data = models.DateTimeField(verbose_name="Время",auto_now_add=True)
    crib = models.CharField(
        "Шпаргалка:\n Воронка 1 : 1./start 2./go 3./ok 4./mes4 5./mes5 6./mes6 7./mes7  8./mes8  9./mes9  10./mes10 "
        "\nВоронка 2 : 2./Vor2_mes2 3./Vor2_mes3 4./Vor2_mes4 5./Vor2_mes5 6./Vor2_mes6 7./Vor2_mes7  8./Vor2_mes8  9./Vor2_mes9 10./Vor2_mes10"
        "\nВоронка 3 : 2./Vor3_mes2 3./Vor3_mes3 4./Vor3_mes4 5./Vor3_mes5 6./Vor3_mes6 7./Vor3_mes7 8./Vor3_mes8 9./Vor3_mes9 10./Vor3_mes10"
        "\nВоронка 4 : 2./Vor4_mes2 3./Vor4_mes3 4./Vor4_mes4 5./Vor4_mes5 6./Vor4_mes6 7./Vor4_mes7 8./Vor4_mes8 9./Vor4_mes9 10./Vor4_mes10"
        "\nВоронка 5 :  2./Vor5_mes2 3./Vor5_mes3 4./Vor5_mes4 5./Vor5_mes5 6./Vor5_mes6 7./Vor5_mes7 8./Vor5_mes8 9./Vor5_mes9 10./Vor5_mes10 ",
        max_length=200, default=1)

    def __str__(self):
        return f'{self.massege}'


    class Meta:
        verbose_name="Voronka3"


class ProfileVor4_bot9(models.Model):
    id = models.PositiveIntegerField(verbose_name="ID пользователя", primary_key=True, unique=True)
    name = models.TextField(verbose_name="Имя пользователя", null=True, blank=False)

    def __str__(self):
        return f'Сообщение{self.pk}'

    class Meta:
        verbose_name = "Профили_Воронки_4"


class MassageVor4_bot9(models.Model):
    name = models.CharField(verbose_name="Название сообщения", null=False, blank=False, max_length=200, )
    massege = models.TextField(verbose_name="Сообщение", null=False, blank=False)
    image = models.ImageField(upload_to="avatars", blank=True,)
    data = models.DateTimeField(verbose_name="Время",auto_now_add=True)
    crib = models.CharField(
        "Шпаргалка:\n Воронка 1 : 1./start 2./go 3./ok 4./mes4 5./mes5 6./mes6 7./mes7  8./mes8  9./mes9  10./mes10 "
        "\nВоронка 2 : 2./Vor2_mes2 3./Vor2_mes3 4./Vor2_mes4 5./Vor2_mes5 6./Vor2_mes6 7./Vor2_mes7  8./Vor2_mes8  9./Vor2_mes9 10./Vor2_mes10"
        "\nВоронка 3 : 2./Vor3_mes2 3./Vor3_mes3 4./Vor3_mes4 5./Vor3_mes5 6./Vor3_mes6 7./Vor3_mes7 8./Vor3_mes8 9./Vor3_mes9 10./Vor3_mes10"
        "\nВоронка 4 : 2./Vor4_mes2 3./Vor4_mes3 4./Vor4_mes4 5./Vor4_mes5 6./Vor4_mes6 7./Vor4_mes7 8./Vor4_mes8 9./Vor4_mes9 10./Vor4_mes10"
        "\nВоронка 5 :  2./Vor5_mes2 3./Vor5_mes3 4./Vor5_mes4 5./Vor5_mes5 6./Vor5_mes6 7./Vor5_mes7 8./Vor5_mes8 9./Vor5_mes9 10./Vor5_mes10 ",
        max_length=200, default=1)

    def __str__(self):
        return f'{self.massege}'


    class Meta:
        verbose_name="Voronka4"

class ProfileVor5_bot9(models.Model):
    id = models.PositiveIntegerField(verbose_name="ID пользователя", primary_key=True, unique=True)
    name = models.TextField(verbose_name="Имя пользователя", null=True, blank=False)

    def __str__(self):
        return f'Сообщение{self.pk}'

    class Meta:
        verbose_name = "Профили_Воронки_5"


class MassageVor5_bot9(models.Model):
    name = models.CharField(verbose_name="Название сообщения", null=False, blank=False, max_length=200, )
    massege = models.TextField(verbose_name="Сообщение", null=False, blank=False)
    image = models.ImageField(upload_to="avatars", blank=True,)
    data = models.DateTimeField(verbose_name="Время",auto_now_add=True)
    crib = models.CharField(
        "Шпаргалка:\n Воронка 1 : 1./start 2./go 3./ok 4./mes4 5./mes5 6./mes6 7./mes7  8./mes8  9./mes9  10./mes10 "
        "\nВоронка 2 : 2./Vor2_mes2 3./Vor2_mes3 4./Vor2_mes4 5./Vor2_mes5 6./Vor2_mes6 7./Vor2_mes7  8./Vor2_mes8  9./Vor2_mes9 10./Vor2_mes10"
        "\nВоронка 3 : 2./Vor3_mes2 3./Vor3_mes3 4./Vor3_mes4 5./Vor3_mes5 6./Vor3_mes6 7./Vor3_mes7 8./Vor3_mes8 9./Vor3_mes9 10./Vor3_mes10"
        "\nВоронка 4 : 2./Vor4_mes2 3./Vor4_mes3 4./Vor4_mes4 5./Vor4_mes5 6./Vor4_mes6 7./Vor4_mes7 8./Vor4_mes8 9./Vor4_mes9 10./Vor4_mes10"
        "\nВоронка 5 :  2./Vor5_mes2 3./Vor5_mes3 4./Vor5_mes4 5./Vor5_mes5 6./Vor5_mes6 7./Vor5_mes7 8./Vor5_mes8 9./Vor5_mes9 10./Vor5_mes10 ",
        max_length=200, default=1)

    def __str__(self):
        return f'{self.massege}'


    class Meta:
        verbose_name="Voronka5"
