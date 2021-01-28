from django.db import models
from django.contrib.auth.models import User
from languages.models import Language, Technology


class Programmer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language, blank=True, null=True)
    technologies = models.ManyToManyField(Technology, blank=True, null=True)
    experience = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f'<{self.user.username}> ({self.user.first_name[0:1]}. {self.user.last_name})'

    def languages_names(self):
        langs = []
        for l in self.languages.all():
            langs.append(l.name)
        return ', '.join(langs)

    def technologies_names(self):
        techs = []
        for l in self.technologies.all():
            techs.append(l.name)
        return ', '.join(techs)

    class Meta:
        ordering = ['user', 'experience']
