from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='src-home'),
    path("user", views.user, name="src-user")
]