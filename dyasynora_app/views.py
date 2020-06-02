from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.db.models import Q

from .models import Project
from .models import Activity
from django.apps import apps
Profile = apps.get_model('users', 'Profile')

from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def home(request):
    context = {
        'projects': Project.objects.all() # Query data from DB
    }
    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)
    return render(request, 'dyasynora_app/diasynora.html', context)

def crowdsourcers(request):
    return render(request, 'dyasynora_app/crowdsourcers.html')

# returns query set object containing a dictionary
def activities_json(request):
    return JsonResponse({
        'activities' : list(Activity.objects.values())
    })

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

class PostDetailView(DetailView):
    model = Project

class UserDetailView(DetailView):
    model = Profile

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'description', 'image', 'location']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['name', 'description', 'image', 'location']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
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

def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'dyasynora_app/detail.html', {'project': project})
"""
def activity(request, project_id):
    response = "You're looking at an activity of project %s."
    return HttpResponse(response % project_id)

# returns query set object containing a dictionary
def projects_json(request):
    return JsonResponse({
        'projects' : list(Project.objects.values())
    })

# returns query set object containing a dictionary
def activities_json(request):
    return JsonResponse({
        'activities' : list(Activity.objects.values())
    })

@csrf_exempt
def new_project(request):
    project_name = request.POST['project_name']
    project_description = request.POST['project_description']
    project_cost = request.POST['project_cost']
    project = Project(project_name = project_name, project_description = project_description, project_cost = project_cost)
    project.save()
    return JsonResponse({
        'id' : project.id,
        'project_name' : project.project_name,
        'project_description' : project.project_description,
        'project_cost' : project.project_cost
    })

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

@csrf_exempt
def delete_project(request,id):
    if request.method == 'DELETE':
        to_delete = Project.objects.filter(id=id)
        to_delete.delete()
    return JsonResponse({'message':"deleted!"}, safe=False)

@csrf_exempt
def update_project(request, id):
    if request.method == 'PUT':
        updated_project = Project.objects.get(id=id)
        input = QueryDict(request.body)
        print(input)
        project_name = input.get('project_name')
        project_description = input.get('project_description')
        project_cost = input.get('project_cost')
        updated_project.project_cost = project_cost
        updated_project.save()
        response = {
            'id' : updated_project.id,
            'project_name' : updated_project.project_name,
            'project_description' : updated_project.project_description,
			'project_cost': updated_project.project_cost
        }
        return JsonResponse(response, safe= False)
"""
