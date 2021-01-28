from rest_framework import serializers
from .models import Language, Technology


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name']


class TechnologySerializer(serializers.ModelSerializer):
    language = LanguageSerializer()

    class Meta:
        model = Technology
        fields = ['id', 'name', 'language']
