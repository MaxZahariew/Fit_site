# from django.db import models
# from django.db import models
# from django.contrib.auth import get_user_model
# from django.urls import reverse
# from django.utils import timezone
# from traitlets import default

# import uuid
# from random import choice
# from datetime import timedelta


# User = get_user_model()


# class Rate(models.Model):
#     # Цены индивидульных тренировок

#     title = models.CharField('Название тарифа', max_length=100)
#     count_minutes = models.SmallIntegerField('Количество минут', null=True)
#     price = models.DecimalField(
#         'Цена', max_digits=10, decimal_places=2, default=1000)
#     description = models.TextField('Описание тарифа', blank=True)

#     class Meta:
#         verbose_name = 'Тариф тренера'
#         verbose_name_plural = 'Тарифы тренеров'
#         ordering = ['-price']

#     def __str__(self):
#         return self.title


# class TrainerImages(models.Model):
#     """Фото тренера"""
#     title = models.CharField("Заголовок", max_length=100, blank=True)
#     description = models.TextField("Описание", blank=True)
#     image = models.ImageField("Изображение", upload_to="trainers/images/")
#     trainer = models.ForeignKey(
#         Trainer, verbose_name="Тренер", on_delete=models.CASCADE, related_name="images")

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = "Фото тренра"
#         verbose_name_plural = "Фото тренеров"


# class RatingStar(models.Model):
#     """Звезда рейтинга"""
#     value = models.SmallIntegerField("Значение", default=0)

#     def __str__(self):
#         return f'{self.value}'

#     class Meta:
#         verbose_name = "Звезда рейтинга"
#         verbose_name_plural = "Звезды рейтинга"
#         ordering = ["-value"]
