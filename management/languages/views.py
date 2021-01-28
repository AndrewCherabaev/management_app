from .models import Language, Technology
from .serializers import LanguageSerializer, TechnologySerializer
from rest_framework import viewsets, permissions


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
