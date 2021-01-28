from django.db import models
from django.contrib.auth.models import User
from languages.models import Language, Technology


class Project(models.Model):
    name = models.TextField(max_length=150)
    participants = models.ManyToManyField(User)

    def __str__(self):
        return f'Project <{self.name}>'

    class Meta:
        ordering = ['name']


class Timesheet(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'Timesheet <{self.date}:{self.user.username}>'

    class Meta:
        ordering = ['project', 'date']
