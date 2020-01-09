from django.contrib import admin

from .models import Country, Indicator, Stat
# Register your models here.
admin.site.register(Country)
admin.site.register(Indicator)
admin.site.register(Stat)
