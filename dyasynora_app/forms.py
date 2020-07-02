from django import forms
from django.contrib.auth.models import User
from .models import Project, Event
from ckeditor.widgets import CKEditorWidget

class ProjectForm(forms.ModelForm):
    story = forms.CharField(widget=CKEditorWidget(config_name='special'), label=' ')

    class Meta:
        model = Project
        fields = ['title','image','story']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['message','project','start_datetime','end_datetime']
