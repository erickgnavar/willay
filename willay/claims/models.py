from django.conf import settings
from django.contrib.gis.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


class Category(TimeStampedModel):

    name = models.CharField(_('Name'), max_length=50)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        default_related_name = 'categories'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Claim(TimeStampedModel, models.Model):

    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    address = models.CharField(_('Address'), max_length=200)
    point = models.PointField(_('Point'), null=True, blank=True)
    date = models.DateTimeField(_('Date'), default=timezone.now)
    description = models.TextField(_('Description'))
    photo = models.ImageField(
        _('Photo'),
        upload_to='claims/claim/photo/%Y/%m/%d/',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _('Claim')
        verbose_name_plural = _('Claims')
        default_related_name = 'claims'
        ordering = ('-date',)

    def __str__(self):
        return f'{self.address} - {self.date}'
