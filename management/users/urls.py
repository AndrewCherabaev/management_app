from .views import ProgrammerViewSet
from rest_framework.routers import DefaultRouter

user_router = DefaultRouter()
user_router.register(r'programmers', ProgrammerViewSet)
