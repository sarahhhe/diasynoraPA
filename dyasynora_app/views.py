from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.db.models import Q

from .models import Project, Campaign, Event, Opportunity
from .models import Activity
from django.apps import apps
Profile = apps.get_model('users', 'Profile')
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from dyasynora_app.forms import ProjectForm, EventForm

from search_views.search import SearchListView
from search_views.filters import BaseFilter

def home(request):
    context = {
        'projects': Project.objects.all() # Query data from DB
    }
    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)
    return render(request, 'dyasynora_app/diasynora.html', context)

class SearchResultsView(ListView):
    model = Project
    template_name = 'dyasynora_app/search_results.html'

    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Project.objects.filter(
            Q(title__icontains=query) | Q(story__icontains=query)
        )
        return object_list

def crowdsourcers(request):
    return render(request, 'dyasynora_app/crowdsourcers.html')

# returns query set object containing a dictionary
def activities_json(request):
    return JsonResponse({
        'activities' : list(Activity.objects.values())
    })

def user_projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects.order_by('-date_created'),
    }
    return render(request, 'dyasynora_app/user_projects.html', context)

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            project = form.save(commit=False)
            project.save()
            return redirect('/')
    else:
        form = ProjectForm()
    return render(request, 'dyasynora_app/project_form.html', {'form': form})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            event = form.save(commit=False)
            event.save()
            return redirect('/')
    else:
        form = EventForm()
    return render(request, 'dyasynora_app/event_form.html', {'form': form})

@csrf_exempt
def new_activity(request):
    activity_name = request.POST['activity_name']
    duration = request.POST['duration']
    activity = Activity(activity_name = activity_name, duration = duration)
    project.save()
    return JsonResponse({
        'id' : activity.id,
        'activity_name' : activity.activity_name,
        'duration' : activity.duration
    })

class PostListView(ListView):
    model = Project
    template_name = 'dyasynora_app/feed.html'
    context_object_name = 'projects'
    ordering = ['-date_created']

class ProjectDetailView(DetailView):
    model = Project
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['campaigns'] = Campaign.objects.all()
        context['events'] = Event.objects.all()
        context['opportunities'] = Opportunity.objects.all()
        return context

class UserDetailView(DetailView):
    model = Profile

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'description', 'image', 'location']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['title', 'image', 'story']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/'

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False

def get_project_queryset(query=None):
    queryset = []
    queries = query.split(" ") #python install 2019 = [python, install, 2019]
    for q in queries:
        project = Project.objects.filter(
            Q(title__icontains=q) |
            Q(body__icontains=q)
        ).distinct()

        for project in projects:
            queryset.append(project)

    return list(set(queryset))

def payment(request):
    return render(request, 'dyasynora_app/payment.html', {'title': 'DiaSynora'})

def our_mission(request):
    return render(request, 'dyasynora_app/our-mission.html', {'title': 'DiaSynora'})

def user_profile(request):
    return render(request, 'dyasynora_app/user-profile.html')

def leaders(request):
    return render(request, 'dyasynora_app/leaders.html', {'title': 'DiaSynora'})

def login(request):
    return render(request, 'dyasynora_app/login.html')

def register(request):
    return render(request, 'dyasynora_app/register.html')

def projects(request):
    latest_project_list = Project.objects.order_by('-date_created')[:5]
    context = {'latest_project_list': latest_project_list}
    return render(request, 'dyasynora_app/projects.html', context)
