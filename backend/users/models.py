from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import CheckConstraint, UniqueConstraint


class User(AbstractUser):
    """Кастомная модель пользователя"""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name',
    )
    email = models.EmailField(
        'Адрес электронной почты',
        max_length=254,
        unique=True,
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Subscribe(models.Model):
    """Модель подписки на авторов"""
    user = models.ForeignKey(
        User,
        related_name='subscriber',
        verbose_name='Подписчик',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        related_name='subscribing',
        verbose_name='Автор',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('-id',)
        constraints = [
            UniqueConstraint(fields=['user', 'author'],
                             name='unique_subscription'),
            CheckConstraint(
                check=~models.Q(user=models.F('author')),
                name='users_cannot_subscribe_themselves')

        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def clean(self):
        if self.user == self.author:
            raise ValidationError(
                'Нельзя подписаться на самого себя')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
