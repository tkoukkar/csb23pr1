from django.urls import path

from . import views

app_name = 'hax'

urlpatterns = [
    path('', views.receive, name='receive'),
]