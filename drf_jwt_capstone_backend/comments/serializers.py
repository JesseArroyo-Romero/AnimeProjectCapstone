from rest_framework import serializers
from .models import Comments

class CommentsSerializer (serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'user', 'anime_id', 'comments']