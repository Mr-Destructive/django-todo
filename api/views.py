from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer
from .models import Todo
from .forms import TaskForm

class CreateTask(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        form = TaskForm()
        return Response({'form': form}, template_name='api/create.html')

    def post(self, request, format=None):
        serializer = TaskSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save(author=request.user)
            return Response({'tasks':serializer.data}, template_name='api/task.html')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateTask(APIView):

    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, pk, format=None):
        form = TaskForm()
        return Response({'form': form}, template_name='api/update.html')

    def post(self, request, pk, format=None):
        task = Todo.objects.get(id=pk)
        serializer = TaskSerializer(instance=task, data=request.data)
        if(serializer.is_valid()):
            serializer.save(author=request.user)
            return Response({'tasks':serializer.data}, template_name='api/task.html')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteTask(APIView):

    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request,pk, format=None):
        task = Todo.objects.get(id=pk)
        task.delete()
        tasks = Todo.objects.filter(author=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response({'tasks':serializer.data}, template_name='base.html')

class Index(APIView):

    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, format=None):
        if request.user.id:
            tasks = Todo.objects.filter(author=request.user)
            serializer = TaskSerializer(tasks, many=True)
            return Response({'tasks':serializer.data}, template_name='base.html')
        return Response(template_name='base.html')

class GetTask(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = (IsAuthenticated,)
    def get(self, request,pk , format=None):
        tasks = Todo.objects.get(id=pk)
        serializer = TaskSerializer(tasks, many=False)
        return Response({'tasks':serializer.data}, template_name='api/task.html')

'''
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

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
'''
