from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    organization = models.ForeignKey('breaks.Organisation', models.RESTRICT, related_name='groups',
                                     verbose_name='Organization')
    name = models.CharField('title', max_length=255)
    manager = models.ForeignKey(User, models.RESTRICT, related_name='group_managers',
                                verbose_name='manager')
    employees = models.ManyToManyField(User, related_name='group_employees', verbose_name='employee',
                                       blank=True)
    min_active = models.PositiveSmallIntegerField('Minimum number of active employees ', null=True, blank=True)
    break_start = models.TimeField('Beginning of lunch', null=True, blank=True)
    break_end = models.TimeField('End of lunch', null=True, blank=True)
    break_max_duration = models.PositiveSmallIntegerField('Maximum duration of lunch', null=True, blank=True)

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.pk})'

    @property
    def break_duration(self):
        return 500
