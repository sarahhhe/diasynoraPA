from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.http import JsonResponse

from django.urls import reverse

from django.conf import settings
# Each class is table in database

class Project(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default='default_proj.jpg', upload_to='project_pics')
    description = models.TextField() # Unrestricted version of CharField
    date_created = models.DateTimeField(default=timezone.now) # actual timezone function is passed
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # if a user is deleted, also delete their projects

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dyasynora_app-project-detail', kwargs={'pk': self.pk})

class Activity(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # if a project is deleted, also delete its activities
    activity_name = models.CharField(max_length=100)
    duration = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now) # actual timezone function is passed

    def __str__(self):
        return self.activity_name
