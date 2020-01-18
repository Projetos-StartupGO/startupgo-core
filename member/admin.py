from django.contrib import admin

from member import models

admin.site.register(models.Member)
admin.site.register(models.Community)
admin.site.register(models.ServiceOffer)
admin.site.register(models.Company)
admin.site.register(models.Event)
