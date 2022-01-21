from django.urls import path
from .views import CreateTask, TaskList
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='index'),
    path('create/', CreateTask.as_view(), name='createtask'),
    path('list/', TaskList.as_view(), name='listview'),
]
