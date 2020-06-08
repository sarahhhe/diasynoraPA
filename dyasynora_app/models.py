from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.http import JsonResponse
from location_field.models.plain import PlainLocationField
from ckeditor_uploader.fields import RichTextUploadingField

from django.urls import reverse

from django.conf import settings
# Each class is table in database
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=29)
    image = models.ImageField(default='default_proj.jpg', upload_to='project_pics')
    description_customisable = RichTextUploadingField(blank=True, null=True, config_name='special')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # if a user is deleted, also delete their projects
    date_created = models.DateTimeField(default=timezone.now) # actual timezone function is passed
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    supporters = models.IntegerField(default=0)
    city = models.CharField(max_length=255, null=True)
    org = models.CharField(max_length=255, null=True)
    org_desc =  models.TextField()
    location = models.CharField(max_length=255, null=True)
    stage = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=29)
    description = models.TextField() # Unrestricted version of CharField

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dyasynora_app-project-detail', kwargs={'pk': self.pk})

class Event(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # if a project is deleted, also delete its volunteering event
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # if a user is deleted, also delete their volunteering instance/link
    start_datetime = models.DateTimeField('%d/%m/%Y %H:%M:%S', blank=True, null=True)
    end_datetime = models.DateTimeField('%d/%m/%Y %H:%M:%S', blank=True, null=True)
    message = models.TextField()

    def add_event(self, event):
        if self.event_set.count() >= 5:
            raise Exception("Too many events on this project")

        self.event_set.add(event)

class Campaign(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True) # if a project is deleted, also delete the campaign
    sponsor_datetime = models.DateTimeField('%d/%m/%Y %H:%M:%S')
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # if a project is deleted, also delete its sponsors

class Opportunity(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True) # if a project is deleted, also delete the opportunity
    opportunity_datetime = models.DateTimeField('%d/%m/%Y %H:%M:%S')
    description = models.TextField()
    message = models.TextField()

class Activity(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # if a project is deleted, also delete its activities
    activity_name = models.CharField(max_length=100)
    duration = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now) # actual timezone function is passed

    def __str__(self):
        return self.activity_name
