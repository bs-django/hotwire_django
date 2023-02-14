from django.urls import path
from . import views

app_name ='stimulus_basic'

urlpatterns = [
    path('counter/', views.counter_view, name='counter'),
]