from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from .models import Todo

class CreateTask(APIView):
    def get(self, request, format=None):
        return render(request,'api/create.html')
    def post(self, request, format=None):
        serializer = TaskSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAS_REQUEST)

class TaskList(APIView):
    def get(self, request, format=None):
        tasks = Todo.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

