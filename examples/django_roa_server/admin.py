from django.contrib import admin

from django.db.models.base import ModelBase
import models
for x in dir(models):
    cls = getattr(models, x)
    if isinstance(cls, ModelBase):
        admin.site.register(cls)
