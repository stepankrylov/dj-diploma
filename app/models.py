from django.db import models


class Phones(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Модель')
    image = models.CharField(max_length=50, verbose_name='Изображение')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    description = models.CharField(max_length=100, verbose_name='Описание')
    slug = models.SlugField(max_length=50)

