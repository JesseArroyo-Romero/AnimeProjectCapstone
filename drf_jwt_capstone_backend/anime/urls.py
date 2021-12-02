from django.urls import path
from . import views

urlpatterns = [
    path('anime/', views.AnimeList.as_view()),
    path('anime/<int:id>/', views.AnimeDetail.as_view()),
]