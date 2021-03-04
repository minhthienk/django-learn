from django.urls import path
from . import views


from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
   path('', views.index, name='home'),
   path('contact/', views.contact, name='contact'),
   path('register/', views.register, name="register"),
]

urlpatterns = [
   path('', views.index),
   path('contact/', views.contact, name='contact'),
   path('register/', views.register, name="register"),
   path('login/', views.login_request, name="login"),
   path('logout/',auth_views.LogoutView.as_view(next_page='/home/'),name='logout'),
]
