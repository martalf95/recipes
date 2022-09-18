from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('list_recipes.urls')),
    path('', include('auth.urls')),
    path('user/', include('user.urls')),
    path('admin', admin.site.urls)
]