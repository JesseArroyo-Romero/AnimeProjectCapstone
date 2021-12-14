from django.urls import path
from . import views

urlpatterns = [
    path('', views.CommentsList.as_view()),
    path('<int:pk>/', views.CommentsDetail.as_view()),
    path('anime/<int:anime_id>/', views.CommentsByAnimeId.as_view()),
]