from rest_framework import serializers
from .models import Anime

class AnimeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['id', 'comment', 'replies', 'title', 'airing', 'synopsis', 'type',
                  'episodes', 'score', 'start_date', 'end_date', 'rated']