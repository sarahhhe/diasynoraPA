from django.urls import path
from . import views
from .views import PostListView, ProjectDetailView, PostCreateView, ProjectUpdateView, ProjectDeleteView, UserDetailView, SearchResultsView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='dyasynora_app-diasynora'),
    path('crowdsourcers/', views.crowdsourcers, name='dyasynora_app-crowdsourcers'),
    path('projects/', PostListView.as_view(), name='dyasynora_app-feed'),
    path('my-projects', views.user_projects, name='user-projects'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='dyasynora_app-project-detail'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='dyasynora_app-profile-detail'),
    path('project/new/', PostCreateView.as_view(), name='dyasynora_app-project-create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='update-project'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='delete-project'),
    path('our-mission/', views.our_mission, name='dyasynora_app-our-mission'),
    path('leaders/', views.leaders, name='dyasynora_app-leaders'),
    path('payment/', views.payment, name='dyasynora_app-payment'),
    path('new_activity/', views.new_activity, name='new activity'),
    path('add/project/', views.add_project, name='project-create'),
    path('add/event/', views.add_event, name='event-create'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
