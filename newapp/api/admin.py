from django.contrib import admin

# Register your models here.

from .models import Note, Name
admin.site.register(Note)
admin.site.register(Name)