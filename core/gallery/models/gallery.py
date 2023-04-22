from django.db import models
from django.contrib.auth import get_user_model


class Gallery(models.Model):
    photo = models.ImageField(
        verbose_name='Картина',
        null=False,
        blank=False,
        upload_to='img'
    )
    signature = models.CharField(
        verbose_name='Подпись',
        null=False,
        blank=False,
    )
    created_at = models.DateTimeField(
        verbose_name='Дата и время создания',
        auto_now_add=True
    )
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    favorite = models.ManyToManyField(
        verbose_name='Избранное',
        to=get_user_model(),
        related_name='favorite'
    )
