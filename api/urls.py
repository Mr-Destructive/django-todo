from django.urls import path
from .views import (
        CreateTask,UpdateTask, DeleteTask, 
        Index, GetTask
        )
from django.views.generic import TemplateView

urlpatterns = [
    #path('', TemplateView.as_view(template_name='base.html'), name='index'),
    path('', Index.as_view(), name='index'),
    path('<str:pk>', GetTask.as_view(), name='task'),
    path('create/', CreateTask.as_view(), name='createtask'),
    path('update/<str:pk>', UpdateTask.as_view(), name='updatetask'),
    path('delete/<str:pk>', DeleteTask.as_view(), name='deletetask'),
]
