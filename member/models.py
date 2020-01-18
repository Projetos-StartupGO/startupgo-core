from uuid import uuid4
from django.db import models as models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser, UserManager


class BaseModel(models.Model):
    id = models.UUIDField(verbose_name=_('id'), default=uuid4, editable=False, unique=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created']


class MemberManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Skill(BaseModel):
    name = models.SlugField()

    class Meta(BaseModel.Meta):
        verbose_name = _('Habilidade')
        verbose_name_plural = _('Habilidades')

    def __str__(self):
        return self.name


class Member(BaseModel, AbstractUser):
    skill = models.ManyToManyField(Skill, related_name='member_skills')

    objects = MemberManager()
    original_manager = UserManager()

    def delete(self, using=None, keep_parents=False):
        raise Exception(_('Membros não podem ser apagados'))

    class Meta(BaseModel.Meta):
        verbose_name = _('Membro')
        verbose_name_plural = _('Membros')

    def __str__(self):
        return self.email


class Community(BaseModel):
    name = models.SlugField()
    description = models.CharField(max_length=255)
    owner = models.ForeignKey(Member, on_delete=models.PROTECT, related_name='community_owners')
    member = models.ManyToManyField(Member, related_name='community_members')

    class Meta(BaseModel.Meta):
        verbose_name = _('Comunidade')
        verbose_name_plural = _('Comunidades')

    def __str__(self):
        return self.name


class Company(BaseModel):
    name = models.SlugField()
    owner = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="company_owners")
    member = models.ManyToManyField(Member, related_name='company_members')

    class Meta(BaseModel.Meta):
        verbose_name = _('Empresa')
        verbose_name_plural = _('Empresas')

    def __str__(self):
        return self.name


class Event(BaseModel):
    name = models.SlugField()
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    owner = models.ForeignKey(Member, on_delete=models.PROTECT, related_name='event_owners')
    community = models.ForeignKey(Community, on_delete=models.PROTECT, related_name='event_communities')

    class Meta(BaseModel.Meta):
        verbose_name = _('Evento')
        verbose_name_plural = _('Eventos')

    def __str__(self):
        return self.name


class Interest(BaseModel):
    name = models.SlugField()

    class Meta(BaseModel.Meta):
        verbose_name = _('Interesse')
        verbose_name_plural = _('Interesses')

    def __str__(self):
        return self.name


class ServiceOffer(BaseModel):
    name = models.SlugField()
    description = models.CharField(max_length=255)
    skill = models.ManyToManyField(Skill, related_name='service_offer_skills')

    class Meta(BaseModel.Meta):
        verbose_name = _('Oferta de serviço')
        verbose_name_plural = _('Oferta de serviços')

    def __str__(self):
        return self.name
