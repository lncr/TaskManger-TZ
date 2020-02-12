from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField(blank=True)
    date_of_creation = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='tasks')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=256)
    date_of_creation = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

