from django.contrib import admin
from .models import MissingPerson,WantedPerson,Tag
# Register your models here.
admin.site.register(MissingPerson)
admin.site.register(WantedPerson)
admin.site.register(Tag)


