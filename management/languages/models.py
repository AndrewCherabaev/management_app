from django.db import models


class Language(models.Model):
    extension = models.CharField(max_length=8)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name} (.{self.extension})'

    class Meta:
        ordering = ['name']


class Technology(models.Model):
    name = models.CharField(max_length=64)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Technologies'
