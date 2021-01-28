from django.contrib import admin
from .models import Project, Timesheet


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Timesheet)
class TimesheetAdmin(admin.ModelAdmin):
    pass
