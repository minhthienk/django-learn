from django.urls import path
from . import views


#path('<int:pk>/', views.PostDetailView.as_view(), name='post'),
urlpatterns = [
    path('', views.PostListView.as_view(), name='blog'),
    path('<int:pk>/', views.post, name='post'),
]

