from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>",views.appointment, name = "appointment"),
    path("", views.home, name = "home"),
    path("create/", views.create, name = "create"),
    path("list/", views.list, name = "list"),
]