from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required

from . import views
from .views import *

app_name = "blog"

urlpatterns = [
    path('', views.PostListView.as_view(), name="list"),
    path('create/', views.PostCreateView.as_view(), name="create"),
    path('<slug:slug>/', views.PostDetailView.as_view(), name="detail"),
    path('<slug:slug>/update/', views.PostUpdateView.as_view(), name="update"),
    path('<slug:slug>/delete/', views.PostDeleteView.as_view(), name="delete"),

    # path('home/', views.index, name="home"),
    # path('', views.HomePageView.as_view(), name="home"),
    # template_name="blog/post_create.html"
    # path('create/', views.PostCreateView.as_view(), name='create'),
    # path('<slug:slug>/<int:pk>/', views.CreateView.as_view(), name="create"),
    # path('<slug:slug>/<int:pk>/delete', views.DeleteView.as_view(), name="delete"),
    # path('<slug:slug>/edit', views.PostDetailView.as_view(), name="edit"),
]
