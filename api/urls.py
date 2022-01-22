from django.urls import path
from .views import CreateTask, TaskList, AddTask
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='index'),
    path('create/', AddTask.as_view(), name='createtask'),
    path('list/', TaskList.as_view(), name='listview'),
]
