from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TimesheetViewSet

projects_router = DefaultRouter()
projects_router.register(r'projects', ProjectViewSet)
projects_router.register(r'timesheets', TimesheetViewSet)
