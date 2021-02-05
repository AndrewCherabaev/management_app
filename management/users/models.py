from django.db import models
from django.contrib.auth.models import User
from languages.models import Language, Technology


class Programmer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language, blank=True, null=True)
    technologies = models.ManyToManyField(Technology, blank=True, null=True)
    _experience = models.BigIntegerField(blank=True, null=True, db_column='experience')

    def __str__(self):
        return f'<{self.user.username}> ({self.user.first_name[0:1]}. {self.user.last_name})'

    def languages_names(self):
        return ', '.join([language.name for language in self.languages.all()])

    def technologies_names(self):
        return ', '.join([technology.name for technology in self.technologies.all()])

    def experience(self):
        experience = self._experience or 0
        years = experience // 365
        months = experience % 365 // 30
        days = experience % 365 % 30

        return f'{years} years {months} months {days} days'

    class Meta:
        ordering = ['user', '_experience']
