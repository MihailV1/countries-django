from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Country(models.Model):
    name  = models.CharField(max_length=100, unique=True)
    languages = models.ManyToManyField(to=Language)  # Добавляем связь многие-ко-многим

    def __str__(self):
        return self.name


