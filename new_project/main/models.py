from django.db import models

# Create your models here.


class Director(models.Model):
    class Meta:
        verbose_name = 'Директора'
        verbose_name_plural = 'Директоры'
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Film(models.Model):
    class Meta:
        ordering = ['-rating', 'title', 'updated']
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
    director = models.ForeignKey(Director, on_delete=models.PROTECT,
                                 related_name="directors", null=True,
                                 verbose_name='Директор')
    title = models.CharField(max_length=100, default="no name", verbose_name='Название')
    regiser = models.CharField(max_length=150, verbose_name='Режисер')
    rating = models.FloatField(verbose_name='Рейтинг')
    dlitelnost = models.IntegerField(verbose_name='Длительность')
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.title
