from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.http import JsonResponse
from location_field.models.plain import PlainLocationField

from django.urls import reverse

from django.conf import settings
# Each class is table in database

class Project(models.Model):
    title = models.CharField(max_length=29)
    name = models.CharField(max_length=29)
    image = models.ImageField(default='default_proj.jpg', upload_to='project_pics')
    description = models.TextField() # Unrestricted version of CharField
    date_created = models.DateTimeField(default=timezone.now) # actual timezone function is passed
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # if a user is deleted, also delete their projects
    city = models.CharField(max_length=255, null=True)
    org = models.CharField(max_length=255, null=True)
    org_desc =  models.TextField()
    location = models.CharField(max_length=255, null=True)
    stage = models.CharField(max_length=100, null=True)
    supporters = models.IntegerField(default=0)

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

class Volunteer(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE) # if an activity is deleted, also delete its volunteering
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # if a user is deleted, also delete their volunteering instance/link
    start_datetime = models.DateTimeField('%d/%m/%Y %H:%M:%S')
    end_datetime = models.DateTimeField('%d/%m/%Y %H:%M:%S')
    message = models.TextField()

class Sponsor(models.Model):
    sponsor = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # if a user is deleted, also delete their sponsoring instance/link
    sponsor_datetime = models.DateTimeField('%d/%m/%Y %H:%M:%S')
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # if a project is deleted, also delete its sponsors

class Mentor(models.Model):
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # if a user is deleted, also delete their sponsoring instance/link
    mentor_datetime = models.DateTimeField('%d/%m/%Y %H:%M:%S')
    description = models.TextField()
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE) # if an activity is deleted, also delete its mentors
