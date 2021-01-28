from .models import Project, Timesheet
from rest_framework.serializers import ModelSerializer
from users.models import User


class ProjectUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ProjectSerializer(ModelSerializer):
    participants = ProjectUserSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'participants']


class TimesheetProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']


class TimesheetSerializer(ModelSerializer):
    user = ProjectUserSerializer(many=False)
    project = TimesheetProjectSerializer(many=False)

    class Meta:
        model = Timesheet
        fields = ['id', 'project', 'date', 'time', 'user']
