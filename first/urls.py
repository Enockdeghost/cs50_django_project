from .  import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index") ,
    path("enock/",views.enock, name="enock"),
    path("<str:names>/",views.name, name="name")
    
]