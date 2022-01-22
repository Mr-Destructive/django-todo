from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from .models import Todo
from .forms import TaskForm

class CreateTask(APIView):
    def get(self, request, format=None):
        form = TaskForm()
        return render(request,'api/create.html', {'form': form})

    def post(self, request, format=None):
        serializer = TaskSerializer(data = request.data)
        print(request.data)
        if(serializer.is_valid()):
            serializer['author']=request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskList(APIView):
    def get(self, request, format=None):
        tasks = Todo.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class AddTask(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TaskForm
    template_name = 'api/create.html'

    def form_valid(self, form):
        print(form)
        form.instance.author = self.request.user
        return super(AddTask, self).form_valid(form)

    def get_success_url(self):
        return reverse('listview')
