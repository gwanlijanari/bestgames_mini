from django.db import models

class Game(models.Model):
    title = models.CharField(unique=True, null=False, blank=False, verbose_name='название')
    genre = models.CharField(unique=True, null=False, blank=False, verbose_name='жанр')
    developer = models.CharField(unique=True, null=False, blank=False, verbose_name='имя')
    price = models.CharField(unique=True, null=False, blank=False, verbose_name='цена')
    rating = models.CharField(unique=True, null=False, blank=False, verbose_name='рейтинг')
    image = models.ImageField(unique=True, null=False, blank=False, verbose_name='название')

