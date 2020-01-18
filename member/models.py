from django.db import models as models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    id = models.UUIDField(verbose_name=_('uuid'), editable=False, unique=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created']


class Member(BaseModel, AbstractUser):

    def delete(self, using=None, keep_parents=False):
        raise Exception(_('Membros não podem ser apagados'))

    class Meta:
        verbose_name = _('Membro')
        verbose_name_plural = _('Membros')


class Community(BaseModel):
    name = models.SlugField()
    description = models.CharField(max_length=255)
    owner = models.ForeignKey(Member, on_delete=models.PROTECT)
    members = models.ForeignKey(Member, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('Comunidade')
        verbose_name_plural = _('Comunidades')


class Company(models.Model):
    name = models.SlugField(populate_from='name', blank=True)
    owner = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="companys")
    members = models.ManyToManyField(Member, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('Empresa')
        verbose_name_plural = _('Empresas')


class Event(models.Model):
    name = models.SlugField()
    address = models.CharField(max_length=255)
    owner = models.ForeignKey(Member, on_delete=models.PROTECT)
    communities = models.ForeignKey(Company, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('Evento')
        verbose_name_plural = _('Eventos')
