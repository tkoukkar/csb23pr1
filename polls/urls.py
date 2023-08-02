# from django.contrib.auth.decorators import login_required    # Required for the fix to broken access control (line 11)
from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), # Allows force browsing as unauthenticated user (FLAW 1)
    # path('<int:pk>/', login_required(views.DetailView.as_view()), name='detail'), # Fix to the above
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('add/', views.add_poll, name='add_poll'),
    path('<int:question_id>/add_choices/', views.add_choices, name='add_choices')
]