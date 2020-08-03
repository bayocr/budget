from django.urls import path

from budget import views

app_name = 'budget'
urlpatterns = [
    path('', views.index, name='index'),
]
