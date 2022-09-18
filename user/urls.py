from django.urls import path
from user import views

urlpatterns = [
  #  path('slug:username', views.user, name="user")
    path('/marta', views.user, name="user")
]
