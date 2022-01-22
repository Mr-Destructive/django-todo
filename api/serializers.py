from rest_framework import serializers
from .models import Todo

class TaskSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Todo
        fields = '__all__'
    
