from django.urls import path, include
# from .views import LanguagesView, index, show
from .views import LanguageViewSet, TechnologyViewSet
from rest_framework.routers import DefaultRouter

language_router = DefaultRouter()
language_router.register(r'languages', LanguageViewSet)
language_router.register(r'technologies', TechnologyViewSet)
