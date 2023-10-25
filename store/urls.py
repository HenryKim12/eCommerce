from django.urls import path
from . import views

urlpatterns = [
    #path('users/', views.UserView.as_view()),
    # path('users/<int:id>', )
    path('login', views.UserLogin.as_view())
]
