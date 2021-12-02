from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.CommentsList.as_view()),
    path('comments/<int:pk>/', views.CommentsDetail.as_view()),
    path('animes_comments/<str:animes_id>/', views.animes_comments())
]