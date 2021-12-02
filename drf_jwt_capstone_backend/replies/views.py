from django.shortcuts import render
from .models import Replies
from .serializers import RepliesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class RepliesList(APIView):

    def get(self, request):
        Replies = Replies.objects.all()
        serializer = RepliesSerializer(Replies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RepliesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RepliesDetail(APIView):

    def get_object(self, pk):
        try:
            return Replies.objects.get(pk=pk)
        except Replies.DoesNotExist:
            raise Http404

    # get by id
    def get(self, request, pk):
        Replies = self.get_object(pk)
        serializer = RepliesSerializer(Replies)
        return Response(serializer.data)

    # update
    def put(self, request, pk):
        Replies = self.get_object(pk)
        serializer = RepliesSerializer(Replies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete
    def delete(self, request, pk):
        Replies = self.get_object(pk)
        Replies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
