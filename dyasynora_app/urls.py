from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', views.home, name='dyasynora_app-diasynora'),
    path('feed/', PostListView.as_view(), name='dyasynora_app-feed'),
    path('project/<int:pk>/', PostDetailView.as_view(), name='dyasynora_app-project-detail'),
    path('project/new/', PostCreateView.as_view(), name='dyasynora_app-project-create'),
    path('project/<int:pk>/update/', PostUpdateView.as_view(), name='dyasynora_app-project-update'),
    path('project/<int:pk>/delete/', PostDeleteView.as_view(), name='dyasynora_app-project-delete'),
    path('our-mission/', views.our_mission, name='dyasynora_app-our-mission'),
]
