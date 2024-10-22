"""MySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from phonebook import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.Main_list.as_view(), name="main_list"),
    path("edit/<slug:pk>/", views.Edit.as_view(), name="edit"),
    #path("delete/<slug:pk>/", views.Delete.as_view(), name="delete"),
    path("create/", views.Create.as_view(), name="create"),
    path("search/", views.Search.as_view(), name="search"),
    path("edit/<slug:pk>/", views.edit, name="edit"),
]