from django.shortcuts import render
from .models import Anime
from .serializers import AnimeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class AnimeList(APIView):
    def get(self, request):
        anime = Anime.objects.all()
        serializer = AnimeSerializer(anime, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class AnimeDetail(APIView):
    def get_object(self, pk):
        try:
            return Anime.objects.get(pk=pk)
        except Anime.DoesNotExist:
            raise Http404

    # get by id
    def get(self, request, pk):
        anime = self.get_object(pk)
        serializer = AnimeSerializer(anime)
        return Response(serializer.data)

    # update
    def put(self, request, pk):
        anime = self.get_object(pk)
        serializer = AnimeSerializer(anime, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        anime = self.get_object(pk)
        anime.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
