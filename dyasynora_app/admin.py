from django.contrib import admin

from .models import Project, Event, Campaign, Opportunity
# Register your models here.

admin.site.register(Project)
admin.site.register(Event)
admin.site.register(Campaign)
admin.site.register(Opportunity)
