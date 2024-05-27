from django.contrib import admin
from .models import Poll, Option

# Register your models here.

admin.site.register(Option)
admin.site.register(Poll)
