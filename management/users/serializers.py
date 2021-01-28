from rest_framework import serializers
from .models import Programmer
from django.contrib.auth.models import User
from languages.serializers import LanguageSerializer, TechnologySerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class ProgrammerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    languages = LanguageSerializer(many=True)
    technologies = TechnologySerializer(many=True)

    class Meta:
        model = Programmer
        fields = ['id', 'user', 'languages', 'technologies', 'experience']
