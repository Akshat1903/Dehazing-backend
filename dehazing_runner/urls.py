from django.urls import path
from . import views

urlpatterns = [
    path('', views.CallImageProcessing.as_view()),
]