from django.urls import path
from . import views

app_name = 'friends'

urlpatterns = [
    path('', views.friends, name="list"),
    path('create/', views.friends_create, name='create'),
    path('<slug>/', views.friends_details, name="details"),
    path('<slug>/comment/', views.add_comment, name="comment"),
]
