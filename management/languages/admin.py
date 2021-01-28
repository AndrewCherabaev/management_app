from django.contrib import admin
from languages.models import Language, Technology


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'extension')


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    empty_value_display = 'N/A'
    list_display = ('name', 'language')
