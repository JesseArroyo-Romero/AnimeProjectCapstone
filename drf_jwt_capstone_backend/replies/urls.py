from django.urls import path
from . import views

urlpatterns = [
    path('', views.RepliesList.as_view()),
    path('<int:pk>/', views.RepliesDetail.as_view()),
    path('anime/<int:comment_id>/', views.RepliesByComment.as_view())
]