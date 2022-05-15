from django.db import models

class Profile(models.Model):
    id = models.PositiveIntegerField(verbose_name="ID пользователя", primary_key=True, unique=True)
    name = models.TextField(verbose_name="Имя пользователя", null=True, blank=False)

    def __str__(self):
        return f'Сообщение{self.pk}'

    class Meta:
        verbose_name = "Профили"


class Massage(models.Model):
    name = models.CharField(verbose_name="Название сообщения", null=False, blank=False, max_length=200, )
    massege = models.TextField(verbose_name="Сообщение", null=False, blank=False)
    image = models.ImageField(upload_to="avatars", blank=True,)
    data = models.DateTimeField(verbose_name="Время",auto_now_add=True)

    def __str__(self):
        return f'{self.massege}'


    class Meta:
        verbose_name="Messages"