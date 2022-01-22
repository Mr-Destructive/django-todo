from rest_framework import serializers
from .models import Todo

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['task', 'status']
