from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.core.serializers import serialize
from .models import Programmer
from rest_framework import viewsets
from .serializers import ProgrammerSerializer


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        serialize('json', Programmer.objects.all()),
        content_type='application/json'
    )


class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.prefetch_related('languages', 'technologies').all()
    serializer_class = ProgrammerSerializer
