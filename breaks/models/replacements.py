from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ReplacementStatus(models.Model):
    code = models.CharField('Code', max_length=16, primary_key=True)
    name = models.CharField('title', max_length=32)
    sort = models.PositiveSmallIntegerField('sorting', null=True, blank=True)
    is_active = models.BooleanField('Activity', default=True)

    class Meta:
        verbose_name = 'ReplacementStatus'
        verbose_name_plural = 'ReplacementsStatus'
        ordering = ('sort',)

    def __str__(self):
        return f'{self.code} {self.name}'


class Replacement(models.Model):
    group = models.ForeignKey('breaks.Group', models.CASCADE, related_name='replacements', verbose_name='Group')

    date = models.DateField('Date replacement')
    break_start = models.TimeField('Beginning of lunch', null=True, blank=True)
    break_end = models.TimeField('End of lunch', null=True, blank=True)
    break_max_duration = models.PositiveSmallIntegerField('Maximum duration of lunch', null=True, blank=True)

    class Meta:
        verbose_name = 'Replacement'
        verbose_name_plural = 'Replacements'
        ordering = ('-date',)

    def __str__(self):
        return f'Смена №{self.pk} для {self.group}'


class ReplacementEmployee(models.Model):
    employee = models.ForeignKey(User, models.CASCADE, related_name='replacements', verbose_name='Employee')
    replacement = models.ForeignKey('breaks.Replacement', models.CASCADE, related_name='employees',
                                    verbose_name='Replacement')
    status = models.ForeignKey('breaks.ReplacementStatus', models.RESTRICT, related_name='replacement_employees',
                                    verbose_name='status')

    class Meta:
        verbose_name = 'Replacement - employee'
        verbose_name_plural = 'Replacements - employees'

    def __str__(self):
        return f'Смена №{self.replacement} для {self.employee}'
