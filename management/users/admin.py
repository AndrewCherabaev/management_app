from django.contrib import admin
from .models import Programmer


@admin.register(Programmer)
class ProgrammerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'languages_names', 'technologies_names', 'experience')
