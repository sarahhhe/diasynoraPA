from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from PIL import Image
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
    title = models.CharField(max_length=50)
    image = models.ImageField(default='default_proj.jpg', upload_to='project_pics')
    story = RichTextUploadingField(blank=True, null=True, config_name='special')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # if a user is deleted, also delete their projects
    date_created = models.DateTimeField(default=timezone.now) # actual timezone function is passed
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    supporters = models.IntegerField(default=0)
    city = models.CharField(max_length=255, blank=True, null=True)
    org = models.CharField(max_length=255, blank=True, null=True)
    org_desc =  models.TextField(blank=True, null=True)
    location = models.CharField(blank=True, max_length=255, null=True)
    stage = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=29, blank=True, null=True)
    description = models.TextField(blank=True, null=True) # Unrestricted version of CharField

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dyasynora_app-project-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Project, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Event(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # if a project is deleted, also delete its volunteering event
    name = models.CharField(max_length=50)
    organiser = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # if a user is deleted, also delete their volunteering instance/link
    start_datetime = models.DateTimeField('%d/%m/%Y %H:%M:%S', blank=True, null=True)
    end_datetime = models.DateTimeField('%d/%m/%Y %H:%M:%S', blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    image = models.ImageField(default='default_proj.jpg', upload_to='event_pics')

    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def add_event(self, event):
        if self.event_set.count() >= 5:
            raise Exception("Too many events on this project")

        self.event_set.add(event)

class Campaign(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True) # if a project is deleted, also delete the campaign
    title = models.CharField(max_length=50)
    organiser = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    campaign_start = models.DateTimeField('%d/%m/%Y', default=timezone.now)
    campaign_end = models.DateTimeField('%d/%m/%Y', default=timezone.now)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True, null=True) # Unrestricted version of CharField
    image = models.ImageField(default='default_proj.jpg', upload_to='campaign_pics')

    def save(self, *args, **kwargs):
        super(Campaign, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Opportunity(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True) # if a project is deleted, also delete the opportunity
    title = models.CharField(max_length=50)
    opportunity_datetime = models.DateTimeField('%d/%m/%Y %H:%M:%S', default=timezone.now)
    description = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    image = models.ImageField(default='default_proj.jpg', upload_to='opportunity_pics')

    def save(self, *args, **kwargs):
        super(Opportunity, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextUploadingField(blank=True, null=True, config_name='special')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_posted = models.DateTimeField(default=timezone.now) # actual timezone function is passed
    category = models.CharField(max_length=50)
class Activity(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # if a project is deleted, also delete its activities
    activity_name = models.CharField(max_length=100)
    duration = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now) # actual timezone function is passed

    def __str__(self):
        return self.activity_name
