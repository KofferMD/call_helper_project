from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Organisation(models.Model):
    name = models.CharField('title', max_length=255)
    director = models.ForeignKey(User, models.RESTRICT, related_name='organisations_directors',
                                 verbose_name='director')
    employees = models.ManyToManyField(User, related_name='organisations_employees', verbose_name='employee',
                                       blank=True)

    class Meta:
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.pk})'


